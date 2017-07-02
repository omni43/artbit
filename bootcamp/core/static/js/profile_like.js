$(function () {
    $(".like").on("click", ".profile_like", function (event) {
        var profile_id = $(this).attr('id')
        var csrf = $(this).attr("csrf");
        $.ajax({
          url: '/profile_like/',
          data: {
            'profile_id': profile_id,
            'csrfmiddlewaretoken': csrf
          },
          type: 'post',
          cache: false,
          success: function (data) {
            $(".like .like-count").text(data);
          }
        });
        return false;
      });
});