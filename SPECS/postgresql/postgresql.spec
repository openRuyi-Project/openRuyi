# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond test 1
%bcond docs 1

%global majorversion 19

Name:           postgresql
Version:        19.0
Release:        %autorelease
Summary:        PostgreSQL client programs
# The PostgreSQL license is very similar to other MIT licenses, but the OSI
# recognizes it as an independent license, so we do as well.
License:        PostgreSQL
URL:            https://www.postgresql.org/
VCS:            git:https://git.postgresql.org/git/postgresql.git
#!RemoteAsset:  sha256:a89fd70efbad6a08c7dbed8d4872e3af30170d9e5ca9dc7906523be95b4e692d
Source0:        https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2
Source1:        Makefile.regress
Source2:        postgresql.pam
Source3:        postgresql-bashprofile
Source4:        postgresql.sysusers
Source5:        postgresql.service
BuildSystem:    meson

# Use runtime sockets outside private temporary directories; https://git.almalinux.org/rpms/postgresql19/src/commit/4152478c89f2be5c28cf24848d825a874694a3a7/postgresql-var-run-socket.patch
Patch2001:      2001-runtime-socket-directory.patch

BuildOption(conf):  --auto-features=disabled
BuildOption(conf):  -Drpath=false
BuildOption(conf):  -Dlibnuma=enabled
BuildOption(conf):  -Dliburing=enabled
BuildOption(conf):  -Dlibcurl=enabled
BuildOption(conf):  -Dldap=enabled
BuildOption(conf):  -Dssl=openssl
BuildOption(conf):  -Dpam=enabled
BuildOption(conf):  -Dgssapi=enabled
BuildOption(conf):  -Duuid=e2fs
BuildOption(conf):  -Dlibxml=enabled
BuildOption(conf):  -Dlibxslt=enabled
BuildOption(conf):  -Dnls=enabled
BuildOption(conf):  -Ddtrace=enabled
BuildOption(conf):  -Dselinux=enabled
BuildOption(conf):  -Dsystem_tzdata=/usr/share/zoneinfo
BuildOption(conf):  -Dsystemd=enabled
BuildOption(conf):  -Dlz4=enabled
BuildOption(conf):  -Dzstd=enabled
BuildOption(conf):  -Dicu=enabled
BuildOption(conf):  -Dplperl=enabled
BuildOption(conf):  -Dpltcl=enabled
BuildOption(conf):  -Dplpython=enabled
BuildOption(conf):  -DPYTHON=%{__python3}
BuildOption(conf):  -Dreadline=enabled
BuildOption(conf):  -Dzlib=enabled
BuildOption(conf):  -Dtap_tests=enabled
BuildOption(conf):  -Ddocs_pdf=disabled
%if %{with docs}
BuildOption(conf):  -Ddocs=enabled
BuildOption(build):  world
%else
BuildOption(conf):  -Ddocs=disabled
%endif

BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  perl-devel
BuildRequires:  perl(Opcode)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  glibc-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  perl
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd
BuildRequires:  pkgconfig(systemd)
BuildRequires:  util-linux
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  gettext
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(pam)
BuildRequires:  systemtap-sdt-devel
BuildRequires:  systemtap-sdt-dtrace
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(icu-uc)

%if %{with docs}
BuildRequires:  docbook-dtds
BuildRequires:  docbook-xsl
BuildRequires:  libxml2
BuildRequires:  libxslt
%endif

Provides:       %{name}-libs = %{version}-%{release}

%description
PostgreSQL is an object-relational database management system.
This package provides client programs and libraries for local and remote servers.
The server and HTML manual are available in postgresql-server and postgresql-doc.

%package        oauth
Summary:        OAuth client authentication for PostgreSQL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    oauth
This module provides the OAuth device authorization flow for libpq clients.
Install it when a PostgreSQL connection requires OAuth authentication.

%package        devel
Summary:        PostgreSQL development header files and libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The postgresql-devel package contains the header files and libraries
needed to compile C or C++ applications which will directly interact
with a PostgreSQL database management server.
You need to install this package if you want to develop applications which
will interact with a PostgreSQL server.

%package        server
Summary:        The programs needed to create and run a PostgreSQL server
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       systemd
Requires:       util-linux
Provides:       %{name}-server(:MODULE_COMPAT_%{majorversion})

%description    server
PostgreSQL is an advanced Object-Relational database management system (DBMS).
The postgresql-server package contains the programs needed to create
and run a PostgreSQL server, which will in turn allow you to create
and maintain PostgreSQL databases.

%if %{with docs}
%package        doc
Summary:        Extra documentation for PostgreSQL
BuildArch:      noarch

%description    doc
This package contains the PostgreSQL HTML manual and tutorial files.
%endif

%package        contrib
Summary:        Extension modules distributed with PostgreSQL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    contrib
The postgresql-contrib package contains various extension modules that are
included in the PostgreSQL distribution.

%package        server-devel
Summary:        PostgreSQL development header files and libraries
Requires:       pkgconfig(icu-uc)
Requires:       pkgconfig(krb5)
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Provides:       postgresql(major) = %{majorversion}

%description    server-devel
The postgresql-server-devel package contains the header files and configuration
needed to compile PostgreSQL server extension.

%package        plperl
Summary:        Perl procedural languages for PostgreSQL
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description    plperl
PL/Perl and PL/PerlU let database functions use Perl. Install this package
and create the required language extension in each database.

%package        pltcl
Summary:        Tcl procedural languages for PostgreSQL
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       tcl%{?_isa}

%description    pltcl
PL/Tcl and PL/TclU let database functions use Tcl. Install this package
and create the required language extension in each database.

%package        plpython3
Summary:        The Python3 procedural language for PostgreSQL
Requires:       %{name}-server%{?_isa} = %{version}-%{release}

%description    plpython3
The postgresql-plpython3 package contains the PL/Python3 procedural language,
which is an extension to the PostgreSQL database server.
Install this if you want to write database functions in Python 3.

%if %{with test}
%package        test
Summary:        The test suite distributed with PostgreSQL
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       %{name}-server-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-contrib%{?_isa} = %{version}-%{release}
Requires:       selinux-tools

%description    test
The postgresql-test package contains files needed for various tests for the
PostgreSQL database management system, including regression tests and
benchmarks.
%endif

%install -a
%if %{with docs}
export DESTDIR=%{buildroot}
%meson_build install-docs
rm -f src/tutorial/.gitignore
%endif

# make sure these directories exist even if we suppressed all contrib modules
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/postgresql/contrib
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/postgresql/extension

install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/postgresql

# PGDATA needs removal of group and world permissions due to pg_pwd hole.
install -d -m 700 $RPM_BUILD_ROOT%{?_localstatedir}/lib/pgsql/data

# backups of data go here
install -d -m 700 $RPM_BUILD_ROOT%{?_localstatedir}/lib/pgsql/backups

# postgres' .bash_profile
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{?_localstatedir}/lib/pgsql/.bash_profile

%if %{with test}
    # tests. There are many files included here that are unnecessary,
    # but include them anyway for completeness.  We replace the original
    # Makefiles, however.
    mkdir -p $RPM_BUILD_ROOT%{_libdir}/postgresql/test
    cp -a src/test/regress $RPM_BUILD_ROOT%{_libdir}/postgresql/test
    install -m 755 %{_vpath_builddir}/src/test/regress/regress.so $RPM_BUILD_ROOT%{_libdir}/postgresql/test/regress/
    # pg_regress binary should be only in one subpackage,
    # there will be a symlink from -test to -devel
    rm -f $RPM_BUILD_ROOT%{_libdir}/postgresql/test/regress/pg_regress
    rm -f $RPM_BUILD_ROOT%{_libdir}/postgresql/test/regress/refint.so
    rm -f $RPM_BUILD_ROOT%{_libdir}/postgresql/test/regress/autoinc.so
    ln -sf ../../pgxs/src/test/regress/pg_regress $RPM_BUILD_ROOT%{_libdir}/postgresql/test/regress/pg_regress
    ln -sf ../../autoinc.so $RPM_BUILD_ROOT%{_libdir}/postgresql/test/regress/autoinc.so
    ln -sf ../../refint.so $RPM_BUILD_ROOT%{_libdir}/postgresql/test/regress/refint.so
    pushd  $RPM_BUILD_ROOT%{_libdir}/postgresql/test/regress
    rm -f .gitignore GNUmakefile Makefile *.o
    chmod 0755 pg_regress regress.so
    popd
    sed -e 's|@bindir@|%{_bindir}|g' -e 's|@sbindir@|%{_sbindir}|g' \
        < %{SOURCE1} \
        > $RPM_BUILD_ROOT%{_libdir}/postgresql/test/regress/Makefile
    chmod 0644 $RPM_BUILD_ROOT%{_libdir}/postgresql/test/regress/Makefile
%endif

# remove files not to be packaged
rm %{buildroot}%{_libdir}/*.a

# Remove extension example docs
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/extension/*.example

%find_lang pg_config-%{majorversion} ecpg-%{majorversion} devel.lst
%find_lang initdb-%{majorversion} pg_basebackup-%{majorversion} pg_controldata-%{majorversion} pg_ctl-%{majorversion} \
    pg_resetwal-%{majorversion} pg_rewind-%{majorversion} plpgsql-%{majorversion} postgres-%{majorversion} \
    pg_checksums-%{majorversion} pg_verifybackup-%{majorversion} pg_combinebackup-%{majorversion} pg_walsummary-%{majorversion} server.lst
%find_lang pg_amcheck-%{majorversion} pg_archivecleanup-%{majorversion} pg_test_fsync-%{majorversion} pg_test_timing-%{majorversion} \
    pg_waldump-%{majorversion} contrib.lst
%find_lang pg_dump-%{majorversion} pg_upgrade-%{majorversion} pgscripts-%{majorversion} psql-%{majorversion} \
    libpq5-%{majorversion} ecpglib6-%{majorversion} main.lst
%find_lang plperl-%{majorversion} plperl.lst
%find_lang pltcl-%{majorversion} pltcl.lst
%find_lang plpython-%{majorversion} plpython3.lst
%if %{with test}
%find_lang postgresql-regress-%{majorversion} test.lst
%else
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/postgresql-regress-%{majorversion}.mo
%endif

install -m0644 -D %{SOURCE4} %{buildroot}%{_sysusersdir}/postgresql.conf
install -m0644 -D %{SOURCE5} %{buildroot}%{_unitdir}/postgresql.service

%pre server
%sysusers_create_package postgresql %{SOURCE4}

%post server
%systemd_post postgresql.service

%preun server
%systemd_preun postgresql.service

%postun server
%systemd_postun postgresql.service

%files -f main.lst
%doc doc/KNOWN_BUGS doc/MISSING_FEATURES doc/TODO
%doc HISTORY
%license COPYRIGHT
%{_bindir}/clusterdb
%{_bindir}/createdb
%{_bindir}/createuser
%{_bindir}/dropdb
%{_bindir}/dropuser
%{_bindir}/pg_dump
%{_bindir}/pg_dumpall
%{_bindir}/pg_isready
%{_bindir}/pg_restore
%{_bindir}/pg_upgrade
%{_bindir}/psql
%{_bindir}/reindexdb
%{_bindir}/vacuumdb
%{_libdir}/libpq.so.*
%{_libdir}/libecpg.so.*
%{_libdir}/libecpg_compat.so.*
%{_libdir}/libpgtypes.so.*

%if %{with docs}
%files doc
%doc src/tutorial
%{_docdir}/%{name}/html/
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man7/*
%license COPYRIGHT
%endif

%files contrib -f contrib.lst
%doc contrib/spi/*.example
%{_bindir}/oid2name
%{_bindir}/pg_amcheck
%{_bindir}/pg_archivecleanup
%{_bindir}/pg_test_fsync
%{_bindir}/pg_test_timing
%{_bindir}/pg_waldump

%{_bindir}/pg_walsummary
%{_bindir}/pg_combinebackup

%{_bindir}/pgbench
%{_bindir}/vacuumlo
%{_datadir}/postgresql/extension/amcheck*
%{_datadir}/postgresql/extension/autoinc*
%{_datadir}/postgresql/extension/bloom*
%{_datadir}/postgresql/extension/btree_gin*
%{_datadir}/postgresql/extension/btree_gist*
%{_datadir}/postgresql/extension/citext*
%{_datadir}/postgresql/extension/cube*
%{_datadir}/postgresql/extension/dblink*
%{_datadir}/postgresql/extension/dict_int*
%{_datadir}/postgresql/extension/dict_xsyn*
%{_datadir}/postgresql/extension/earthdistance*
%{_datadir}/postgresql/extension/file_fdw*
%{_datadir}/postgresql/extension/fuzzystrmatch*
%{_datadir}/postgresql/extension/hstore.control
%{_datadir}/postgresql/extension/hstore--*.sql
%{_datadir}/postgresql/extension/insert_username*
%{_datadir}/postgresql/extension/intagg*
%{_datadir}/postgresql/extension/intarray*
%{_datadir}/postgresql/extension/isn*
%{_datadir}/postgresql/extension/lo*
%{_datadir}/postgresql/extension/pg_logicalinspect*
%{_datadir}/postgresql/extension/ltree.control
%{_datadir}/postgresql/extension/ltree--*.sql
%{_datadir}/postgresql/extension/moddatetime*
%{_datadir}/postgresql/extension/pageinspect*
%{_datadir}/postgresql/extension/pg_buffercache*
%{_datadir}/postgresql/extension/pg_freespacemap*
%{_datadir}/postgresql/extension/pg_prewarm*
%{_datadir}/postgresql/extension/pg_stash_advice*
%{_datadir}/postgresql/extension/pg_stat_statements*
%{_datadir}/postgresql/extension/pg_surgery*
%{_datadir}/postgresql/extension/pg_trgm*
%{_datadir}/postgresql/extension/pg_visibility*
%{_datadir}/postgresql/extension/pg_walinspect*
%{_datadir}/postgresql/extension/pgcrypto*
%{_datadir}/postgresql/extension/pgrowlocks*
%{_datadir}/postgresql/extension/pgstattuple*
%{_datadir}/postgresql/extension/postgres_fdw*
%{_datadir}/postgresql/extension/refint*
%{_datadir}/postgresql/extension/seg*
%{_datadir}/postgresql/extension/tablefunc*
%{_datadir}/postgresql/extension/tcn*
%{_datadir}/postgresql/extension/tsm_system_rows*
%{_datadir}/postgresql/extension/tsm_system_time*
%{_datadir}/postgresql/extension/unaccent*
%{_libdir}/postgresql/_int.so
%{_libdir}/postgresql/amcheck.so
%{_libdir}/postgresql/auth_delay.so
%{_libdir}/postgresql/auto_explain.so
%{_libdir}/postgresql/autoinc.so
%{_libdir}/postgresql/bloom.so
%{_libdir}/postgresql/btree_gin.so
%{_libdir}/postgresql/btree_gist.so
%{_libdir}/postgresql/citext.so
%{_libdir}/postgresql/cube.so
%{_libdir}/postgresql/dblink.so
%{_libdir}/postgresql/dict_int.so
%{_libdir}/postgresql/dict_xsyn.so
%{_libdir}/postgresql/earthdistance.so
%{_libdir}/postgresql/file_fdw.so
%{_libdir}/postgresql/fuzzystrmatch.so
%{_libdir}/postgresql/hstore.so
%{_libdir}/postgresql/insert_username.so
%{_libdir}/postgresql/isn.so
%{_libdir}/postgresql/lo.so
%{_libdir}/postgresql/ltree.so
%{_libdir}/postgresql/pg_logicalinspect.so
%{_libdir}/postgresql/pg_overexplain.so
%{_libdir}/postgresql/pg_plan_advice.so
%{_libdir}/postgresql/pg_stash_advice.so
%{_libdir}/postgresql/moddatetime.so
%{_libdir}/postgresql/pageinspect.so
%{_libdir}/postgresql/passwordcheck.so
%{_libdir}/postgresql/pg_buffercache.so
%{_libdir}/postgresql/pg_freespacemap.so
%{_libdir}/postgresql/pg_prewarm.so
%{_libdir}/postgresql/pg_stat_statements.so
%{_libdir}/postgresql/pg_surgery.so
%{_libdir}/postgresql/pg_trgm.so
%{_libdir}/postgresql/pg_visibility.so
%{_libdir}/postgresql/pg_walinspect.so
%{_libdir}/postgresql/basic_archive.so
%{_libdir}/postgresql/basebackup_to_shell.so
%{_libdir}/postgresql/pgcrypto.so
%{_libdir}/postgresql/pgrowlocks.so
%{_libdir}/postgresql/pgstattuple.so
%{_libdir}/postgresql/postgres_fdw.so
%{_libdir}/postgresql/refint.so
%{_libdir}/postgresql/seg.so
%{_libdir}/postgresql/tablefunc.so
%{_libdir}/postgresql/tcn.so
%{_libdir}/postgresql/test_decoding.so
%{_libdir}/postgresql/tsm_system_rows.so
%{_libdir}/postgresql/tsm_system_time.so
%{_libdir}/postgresql/unaccent.so
%{_datadir}/postgresql/contrib/sepgsql.sql
%{_libdir}/postgresql/sepgsql.so
%{_datadir}/postgresql/extension/sslinfo*
%{_libdir}/postgresql/sslinfo.so
%{_datadir}/postgresql/extension/uuid-ossp*
%{_libdir}/postgresql/uuid-ossp.so
%{_datadir}/postgresql/extension/xml2*
%{_libdir}/postgresql/pgxml.so

%files server -f server.lst
%{_bindir}/initdb
%{_bindir}/pg_basebackup

%{_bindir}/pg_controldata
%{_bindir}/pg_ctl
%{_bindir}/pg_receivewal
%{_bindir}/pg_recvlogical
%{_bindir}/pg_resetwal
%{_bindir}/pg_rewind
%{_bindir}/pg_checksums
%{_bindir}/pg_verifybackup

%{_bindir}/pg_createsubscriber

%{_bindir}/postgres
%dir %{_datadir}/postgresql
%{_datadir}/postgresql/*.sample
%dir %{_datadir}/postgresql/contrib
%dir %{_datadir}/postgresql/extension
%{_datadir}/postgresql/extension/plpgsql*
%{_datadir}/postgresql/information_schema.sql
%{_datadir}/postgresql/postgres.bki
%{_datadir}/postgresql/snowball_create.sql
%{_datadir}/postgresql/sql_features.txt
%{_datadir}/postgresql/system_constraints.sql
%{_datadir}/postgresql/system_functions.sql
%{_datadir}/postgresql/system_views.sql
%{_datadir}/postgresql/timezonesets/
%{_datadir}/postgresql/tsearch_data/
%dir %{_libdir}/postgresql
%{_libdir}/postgresql/*_and_*.so
%{_libdir}/postgresql/dict_snowball.so
%{_libdir}/postgresql/cyrillic.so
%{_libdir}/postgresql/euc2004_sjis2004.so
%{_libdir}/postgresql/libpqwalreceiver.so
%{_libdir}/postgresql/pgoutput.so
%{_libdir}/postgresql/pgrepack.so
%{_libdir}/postgresql/plpgsql.so

%attr(700,postgres,postgres) %dir %{?_localstatedir}/lib/pgsql
%attr(644,postgres,postgres) %config(noreplace) %{?_localstatedir}/lib/pgsql/.bash_profile
%attr(700,postgres,postgres) %dir %{?_localstatedir}/lib/pgsql/backups
%attr(700,postgres,postgres) %dir %{?_localstatedir}/lib/pgsql/data
%ghost %attr(755,postgres,postgres) %dir %{_rundir}/postgresql
%config(noreplace) /etc/pam.d/postgresql
%{_sysusersdir}/postgresql.conf
%{_unitdir}/postgresql.service

%files server-devel
%dir %{_datadir}/postgresql
%{_datadir}/postgresql/errcodes.txt
%dir %{_includedir}/postgresql
%{_includedir}/postgresql/server
%{_libdir}/postgresql/pgxs/

%files oauth
%license COPYRIGHT
%{_libdir}/libpq-oauth.so

%files devel -f devel.lst
%{_bindir}/ecpg
%{_includedir}/ecpg*.h
%{_includedir}/pgtypes*.h
%{_includedir}/sqlca.h
%{_includedir}/sql3types.h
%{_includedir}/sqlda*.h
%{_includedir}/postgresql/informix/
%{_libdir}/libecpg.so
%{_libdir}/libecpg_compat.so
%{_libdir}/libpgtypes.so
%{_libdir}/pkgconfig/libecpg.pc
%{_libdir}/pkgconfig/libecpg_compat.pc
%{_libdir}/pkgconfig/libpgtypes.pc
%{_bindir}/pg_config
%{_includedir}/libpq-events.h
%{_includedir}/libpq-fe.h
%{_includedir}/postgres_ext.h
%{_includedir}/postgresql/internal/*.h
%{_includedir}/postgresql/internal/libpq/pqcomm.h

%{_includedir}/postgresql/internal/libpq/protocol.h

%{_includedir}/libpq/*.h
%{_libdir}/pkgconfig/libpq.pc
%{_libdir}/libpq.so
%{_includedir}/pg_config*.h

%files plperl -f plperl.lst
%license COPYRIGHT
%{_datadir}/postgresql/extension/plperl*
%{_libdir}/postgresql/plperl.so

%{_datadir}/postgresql/extension/bool_plperl*
%{_datadir}/postgresql/extension/hstore_plperl*
%{_datadir}/postgresql/extension/jsonb_plperl*
%{_libdir}/postgresql/bool_plperl.so
%{_libdir}/postgresql/hstore_plperl.so
%{_libdir}/postgresql/jsonb_plperl.so

%files pltcl -f pltcl.lst
%license COPYRIGHT
%{_datadir}/postgresql/extension/pltcl*
%{_libdir}/postgresql/pltcl.so

%files plpython3 -f plpython3.lst
%{_datadir}/postgresql/extension/plpython3*
%{_libdir}/postgresql/plpython3.so
%{_datadir}/postgresql/extension/hstore_plpython3u*
%{_datadir}/postgresql/extension/jsonb_plpython3u*
%{_datadir}/postgresql/extension/ltree_plpython3u*
%{_libdir}/postgresql/hstore_plpython3.so
%{_libdir}/postgresql/jsonb_plpython3.so
%{_libdir}/postgresql/ltree_plpython3.so

%if %{with test}
%files test -f test.lst
%attr(-,postgres,postgres) %{_libdir}/postgresql/test
%endif

%changelog
%autochangelog
