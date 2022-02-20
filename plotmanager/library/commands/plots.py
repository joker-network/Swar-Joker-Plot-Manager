import logging


def create(*args, joker_location='joker', backend='joker', **kwargs):
    backend_command = _get_backend_command(backend, joker_location)
    backend_flags = _get_backend_flags(backend, *args, **kwargs)

    for key, value in backend_flags.items():
        flag = f'-{key}'
        backend_command.append(flag)
        if value == '':
            continue
        backend_command.append(str(value))

    return backend_command


def _get_backend_command(backend, joker_location):
    logging.debug(f'Parsing backend commands for {backend}')

    backend_commands = dict(
        joker=[joker_location, 'plots', 'create'],
        madmax=[joker_location],
    )

    return backend_commands.get(backend)


def _get_backend_flags(backend, *args, **kwargs):
    logging.debug(f'Parsing backend flags for {backend}')

    backend_parsers = dict(
        joker=_get_joker_flags,
        madmax=_get_madmax_flags,
    )
    backend_parser = backend_parsers.get(backend)

    return backend_parser(*args, **kwargs)


def _get_joker_flags(size, memory_buffer, temporary_directory, destination_directory, threads, buckets, bitfield,
                     temporary2_directory=None, farmer_public_key=None, pool_public_key=None,
                     exclude_final_directory=False, pool_contract_address=None, **kwargs):
    flags = dict(
        k=size,
        b=memory_buffer,
        t=temporary_directory,
        d=destination_directory,
        r=threads,
        u=buckets,
    )

    if temporary2_directory is not None:
        flags['2'] = temporary2_directory
    if farmer_public_key is not None:
        flags['f'] = farmer_public_key
    if pool_public_key is not None:
        flags['p'] = pool_public_key
    if bitfield is False:
        flags['e'] = ''
    if exclude_final_directory:
        flags['x'] = ''
    if pool_contract_address is not None:
        flags['c'] = pool_contract_address

    return flags


def _get_madmax_flags(temporary_directory, destination_directory, threads, buckets,
                      buckets_p3=None, threadX_p2=None, temporary2_directory=None, farmer_public_key=None,
                      pool_public_key=None, pool_contract_address=None, **kwargs):
    flags = dict(
        r=threads,
        t=temporary_directory,
        d=destination_directory,
        u=buckets,
    )

    if temporary2_directory is not None:
        flags['2'] = temporary2_directory
    if farmer_public_key is not None:
        flags['f'] = farmer_public_key
    if pool_public_key is not None:
        flags['p'] = pool_public_key
    if pool_contract_address is not None:
        flags['c'] = pool_contract_address
    if buckets_p3 is not None:
        flags['v'] = buckets_p3
    if threadX_p2 is not None:
        flags['K'] = threadX_p2

    return flags
