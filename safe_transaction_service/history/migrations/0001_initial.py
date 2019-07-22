# Generated by Django 2.2.2 on 2019-06-18 16:13

import django.db.models.deletion
import django.utils.timezone
import gnosis.eth.django.models
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultisigTransaction',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('safe_tx_hash', gnosis.eth.django.models.Sha3HashField(primary_key=True, serialize=False)),
                ('safe', gnosis.eth.django.models.EthereumAddressField()),
                ('to', gnosis.eth.django.models.EthereumAddressField()),
                ('value', gnosis.eth.django.models.Uint256Field()),
                ('data', models.BinaryField(null=True)),
                ('operation', models.PositiveSmallIntegerField(choices=[(0, 'CALL'), (1, 'DELEGATE_CALL'), (2, 'CREATE')])),
                ('safe_tx_gas', gnosis.eth.django.models.Uint256Field()),
                ('base_gas', gnosis.eth.django.models.Uint256Field()),
                ('gas_price', gnosis.eth.django.models.Uint256Field()),
                ('gas_token', gnosis.eth.django.models.EthereumAddressField(null=True)),
                ('refund_receiver', gnosis.eth.django.models.EthereumAddressField(null=True)),
                ('nonce', gnosis.eth.django.models.Uint256Field()),
                ('mined', models.BooleanField(default=False)),
                ('execution_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MultisigConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('owner', gnosis.eth.django.models.EthereumAddressField()),
                ('transaction_hash', gnosis.eth.django.models.Sha3HashField()),
                ('confirmation_type', models.PositiveSmallIntegerField(choices=[(0, 'CONFIRMATION'), (1, 'EXECUTION')])),
                ('block_number', gnosis.eth.django.models.Uint256Field()),
                ('block_date_time', models.DateTimeField()),
                ('mined', models.BooleanField(default=False)),
                ('multisig_transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirmations', to='history.MultisigTransaction')),
            ],
            options={
                'unique_together': {('multisig_transaction', 'owner', 'confirmation_type')},
            },
        ),
    ]
