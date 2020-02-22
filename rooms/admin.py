from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")},),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Detailse", {"fields": ("host",)}),
    )

    list_display = [
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    ]

    list_filter = [
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    ]

    search_fields = ["^city", "^host__username"]

    filter_horizontal = ["amenities", "facilities", "house_rules"]

    # 두 번째 인자인 obj는 현재 row(admin 패널에서의 행)을 의미한다.
    def count_amenities(self, obj):
        print(obj.amenities.all())
        return "potato"

    count_amenities.short_description = "hello"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ """

    pass

