from django.db import models
from django.core import validators
from django.utils import timezone

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # 名前
    customer_name = models.CharField(
        verbose_name='名前',
        max_length=16,
        blank=True,
        null=True,
    )

    # カナ
    customer_kana = models.CharField(
        verbose_name='カナ',
        max_length=16,
        blank=True,
        null=True,
    )

    # 郵便番号    
    customer_post_code = models.IntegerField(
        verbose_name='郵便番号',
        blank=True,
        null=True,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(9999999)]
    )

    # 住所
    customer_address = models.CharField(
        verbose_name='住所',
        max_length=64,
        blank=True,
        null=True,
    )

    # 電話番号
    customer_tel_number = models.CharField(
        verbose_name='電話番号',
        max_length=14,
        blank=True,
        null=True,
    )

    # メモ
    customer_memo = models.TextField(
        verbose_name='メモ',
        blank=True,
        null=True,
    )

    # タイムスタンプ
    customer_timestamp = models.DateTimeField(
        verbose_name='タイムスタンプ',
        auto_now = True # 登録時と更新時に現在時間を設定
    )

    
    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    # def __str__(self):
    #     """
    #     リストボックスや管理画面での表示
    #     """
    #     return self.sample_1

    def __str__(self):
        return self.customer_name

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = verbose_name_plural = '顧客'
