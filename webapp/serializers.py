from rest_framework import serializers
from .models import Movies,Genre


class GenreSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)

    class Meta:
        model = Genre
        fields = ('id',
                  'category',)


class MoviesSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    class Meta:
        model = Movies
        fields = (
            # 'id',
            'popularity',
            'director',
            'genre',
            'imdb_score',
            'name',
        )
    def create(self, validated_data):
        genre = validated_data.pop('genre')
        movie = Movies.objects.create(**validated_data)
        for gn in genre:
            gn_data = Genre.objects.get(**gn)
            movie.genre.add(gn_data)
        return movie

    def update(self, instance, validated_data):
        genre = validated_data.pop('genre')
        instance.popularity = validated_data.get('popularity', instance.popularity)
        instance.director = validated_data.get('director', instance.director)
        instance.imdb_score = validated_data.get('imdb_score', instance.imdb_score)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        keep_genre = []
        for gn in genre:
            if "id" in gn.keys():
                if Genre.objects.filter(id=gn["id"]).exists():
                    c = Genre.objects.get(id=gn["id"])
                    c.category = gn.get('category', c.category)
                    c.save()
                    keep_genre.append(c.id)
                else:
                    continue
            else:
                c = Genre.objects.get(**gn)
                instance.genre.add(c)
                keep_genre.append(c.id)

        for gn in instance.genre.all():
            if gn.id not in keep_genre:
                gn.delete()

        return instance

