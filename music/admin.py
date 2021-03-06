from django.contrib import admin

from .models import Band, Album, Song, LikedByUsers


class AlbumInline(admin.TabularInline):
    model = Album
    fields = ['name']
    show_change_link = True
    extra = 0


class SongInline(admin.TabularInline):
    model = Song
    fields = ['name', 'song_file']
    show_change_link = True
    extra = 0


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'albums', 'songs', 'popularity')
    list_filter = ('name', 'popularity')
    search_fields = ('name',)
    ordering = ['name']

    fields = ('name', 'popularity', 'description', 'image', 'image_tag',)
    readonly_fields = ('popularity', 'image_tag',)

    inlines = [
        AlbumInline,
    ]

    def albums(self, obj):
        return len(obj.album_set.all())

    def songs(self, obj):
        return len(obj.song_set.all())


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'band', 'songs')
    list_filter = ('name', 'band')
    search_fields = ('name', 'band')
    ordering = ('name', 'band')

    fields = ('name', 'band', 'image', 'image_tag',)
    readonly_fields = ('image_tag',)

    inlines = [SongInline]

    def songs(self, obj):
        return len(obj.song_set.all())


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'band', 'album', 'duration')
    list_filter = ('name', 'band', 'album')
    search_field = ('name', 'band', 'album', 'lyrics')
    ordering = ('name', 'band', 'album')

    fields = ('name', 'duration', 'band', 'album', 'lyrics', 'song_file', 'song_tag')
    readonly_fields = ('song_tag', 'duration')


admin.site.register(Band, BandAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(LikedByUsers)
