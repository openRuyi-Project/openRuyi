# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond test 0
%bcond docs 0

%global majorversion 18
%global service_name postgresql.service

Name:           postgresql
Version:        18.1
Release:        %autorelease
Summary:        PostgreSQL client programs
# The PostgreSQL license is very similar to other MIT licenses, but the OSI
# recognizes it as an independent license, so we do as well.
License:        PostgreSQL
Url:            http://www.postgresql.org/
VCS:            git:https://git.postgresql.org/git/postgresql.git
#!RemoteAsset:  sha256:ff86675c336c46e98ac991ebb306d1b67621ece1d06787beaade312c2c915d54
Source0:        https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2
Source1:        Makefile.regress
Source2:        postgresql.pam
Source3:        postgresql-bashprofile
Source4:        postgresql.sysusers
Source5:        postgresql.tmpfiles
Source6:        postgresql.service
BuildSystem:    autotools

# Comments for these patches are in the patch files.
Patch0:         rpm-pgsql.patch
Patch1:         postgresql-var-run-socket.patch
Patch2:         postgresql-no-libecpg.patch

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --with-ldap
BuildOption(conf):  --with-openssl
BuildOption(conf):  --with-pam
BuildOption(conf):  --with-gssapi
BuildOption(conf):  --with-ossp-uuid
BuildOption(conf):  --with-libxml
BuildOption(conf):  --with-libxslt
BuildOption(conf):  --enable-nls
BuildOption(conf):  --enable-dtrace
BuildOption(conf):  --with-selinux
BuildOption(conf):  --with-system-tzdata=/usr/share/zoneinfo
BuildOption(conf):  --datadir=%_datadir/pgsql
BuildOption(conf):  --with-systemd
BuildOption(conf):  --with-lz4
BuildOption(conf):  --with-zstd
BuildOption(conf):  --with-icu
BuildOption(conf):  --with-python

BuildRequires:  make
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  glibc-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  perl
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd
BuildRequires:  pkgconfig(systemd)
BuildRequires:  util-linux
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  gettext
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(pam)
BuildRequires:  systemtap-sdt-devel
BuildRequires:  systemtap-sdt-dtrace
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(icu-uc)

%if %{with docs}
BuildRequires:  docbook-xsl
%endif

Provides:       %{name}-libs = %{version}-%{release}

%description
PostgreSQL is an advanced Object-Relational database management system (DBMS).
The base postgresql package contains the client programs that you'll need to
access a PostgreSQL DBMS server, as well as HTML documentation for the whole
system.  These client programs can be located on the same machine as the
PostgreSQL server, or on a remote machine that accesses a PostgreSQL server
over a network connection.  The PostgreSQL server can be found in the
postgresql-server sub-package.

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
# We require this to be present for %%{_prefix}/lib/tmpfiles.d
Requires:       systemd
# We require this to be present for /usr/sbin/runuser when using --initdb (rhbz#2071437)
Requires:       util-linux
# postgresql setup requires runuser from util-linux package
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
The postgresql-doc package contains some additional documentation for
PostgreSQL.  Currently, this includes the main documentation in PDF format
and source files for the PostgreSQL tutorial.
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

%description    server-devel
The postgresql-server-devel package contains the header files and configuration
needed to compile PostgreSQL server extension.

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

%description    test
The postgresql-test package contains files needed for various tests for the
PostgreSQL database management system, including regression tests and
benchmarks.
%endif

%prep
%autosetup -n postgresql-%{version} -p1

%build -a
%make_build -C contrib

%if %{with test}
    make all -C src/test/regress
%endif

%install -a
%make_install -C contrib

# make sure these directories exist even if we suppressed all contrib modules
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pgsql/contrib
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pgsql/extension

install -d $RPM_BUILD_ROOT/etc/pam.d
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/postgresql

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
    mkdir -p $RPM_BUILD_ROOT%{_libdir}/pgsql/test
    cp -a src/test/regress $RPM_BUILD_ROOT%{_libdir}/pgsql/test
    # pg_regress binary should be only in one subpackage,
    # there will be a symlink from -test to -devel
    rm -f $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/pg_regress
    rm -f $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/refint.so
    rm -f $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/autoinc.so
    ln -sf ../../pgxs/src/test/regress/pg_regress $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/pg_regress
    ln -sf ../../autoinc.so $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/autoinc.so
    ln -sf ../../refint.so $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/refint.so
    pushd  $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress
    rm -f GNUmakefile Makefile *.o
    chmod 0755 pg_regress regress.so
    popd
    sed 's|@bindir@|%{_bindir}|g' \
        < %{SOURCE1} \
        > $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/Makefile
    chmod 0644 $RPM_BUILD_ROOT%{_libdir}/pgsql/test/regress/Makefile
%endif

# remove files not to be packaged
rm %{buildroot}%{_libdir}/*.a

# Remove extension example docs
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/pgsql/extension/*.example

find_lang_bins ()
{
    lstfile=$1 ; shift
    cp /dev/null "$lstfile"
    for binary; do
        %find_lang "$binary"-%{majorversion}
        cat "$binary"-%{majorversion}.lang >>"$lstfile"
    done
}
find_lang_bins devel.lst pg_config
find_lang_bins server.lst \
    initdb pg_basebackup pg_controldata pg_ctl pg_resetwal pg_rewind plpgsql \
    postgres pg_checksums pg_verifybackup pg_combinebackup \
    pg_walsummary
find_lang_bins contrib.lst \
    pg_amcheck pg_archivecleanup pg_test_fsync pg_test_timing pg_waldump
find_lang_bins main.lst \
    pg_dump pg_upgrade pgscripts psql \
libpq5

find_lang_bins plpython3.lst plpython

install -m0644 -D %{SOURCE4} %{buildroot}%{_sysusersdir}/postgresql.conf
install -m0644 -D %{SOURCE5} %{buildroot}%{_tmpfilesdir}/postgresql.conf
install -m0644 -D %{SOURCE6} %{buildroot}%{_unitdir}/postgresql.service

%pre server
%sysusers_create_package postgresql postgresql.sysusers.conf
%tmpfiles_create_package postgresql postgresql.tmpfiles.conf

%post server
%systemd_post %service_name

%preun server
%systemd_preun %service_name

%postun server
%systemd_postun_with_restart %service_name

%files -f main.lst
%doc doc/KNOWN_BUGS doc/MISSING_FEATURES doc/TODO
%doc COPYRIGHT HISTORY
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

%if %{with docs}
%files doc
%doc doc/html
%{_libdir}/pgsql/tutorial/
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
%{_datadir}/pgsql/extension/amcheck*
%{_datadir}/pgsql/extension/autoinc*
%{_datadir}/pgsql/extension/bloom*
%{_datadir}/pgsql/extension/btree_gin*
%{_datadir}/pgsql/extension/btree_gist*
%{_datadir}/pgsql/extension/citext*
%{_datadir}/pgsql/extension/cube*
%{_datadir}/pgsql/extension/dblink*
%{_datadir}/pgsql/extension/dict_int*
%{_datadir}/pgsql/extension/dict_xsyn*
%{_datadir}/pgsql/extension/earthdistance*
%{_datadir}/pgsql/extension/file_fdw*
%{_datadir}/pgsql/extension/fuzzystrmatch*
%{_datadir}/pgsql/extension/hstore*
%{_datadir}/pgsql/extension/insert_username*
%{_datadir}/pgsql/extension/intagg*
%{_datadir}/pgsql/extension/intarray*
%{_datadir}/pgsql/extension/isn*
%{_datadir}/pgsql/extension/jsonb_plpython3u*
%{_datadir}/pgsql/extension/lo*
%{_datadir}/pgsql/extension/pg_logicalinspect*
%{_datadir}/pgsql/extension/ltree*
%{_datadir}/pgsql/extension/moddatetime*
%{_datadir}/pgsql/extension/pageinspect*
%{_datadir}/pgsql/extension/pg_buffercache*
%{_datadir}/pgsql/extension/pg_freespacemap*
%{_datadir}/pgsql/extension/pg_prewarm*
%{_datadir}/pgsql/extension/pg_stat_statements*
%{_datadir}/pgsql/extension/pg_surgery*
%{_datadir}/pgsql/extension/pg_trgm*
%{_datadir}/pgsql/extension/pg_visibility*
%{_datadir}/pgsql/extension/pg_walinspect*
%{_datadir}/pgsql/extension/pgcrypto*
%{_datadir}/pgsql/extension/pgrowlocks*
%{_datadir}/pgsql/extension/pgstattuple*
%{_datadir}/pgsql/extension/postgres_fdw*
%{_datadir}/pgsql/extension/refint*
%{_datadir}/pgsql/extension/seg*
%{_datadir}/pgsql/extension/tablefunc*
%{_datadir}/pgsql/extension/tcn*
%{_datadir}/pgsql/extension/tsm_system_rows*
%{_datadir}/pgsql/extension/tsm_system_time*
%{_datadir}/pgsql/extension/unaccent*
%{_libdir}/pgsql/_int.so
%{_libdir}/pgsql/amcheck.so
%{_libdir}/pgsql/auth_delay.so
%{_libdir}/pgsql/auto_explain.so
%{_libdir}/pgsql/autoinc.so
%{_libdir}/pgsql/bloom.so
%{_libdir}/pgsql/btree_gin.so
%{_libdir}/pgsql/btree_gist.so
%{_libdir}/pgsql/citext.so
%{_libdir}/pgsql/cube.so
%{_libdir}/pgsql/dblink.so
%{_libdir}/pgsql/dict_int.so
%{_libdir}/pgsql/dict_xsyn.so
%{_libdir}/pgsql/earthdistance.so
%{_libdir}/pgsql/file_fdw.so
%{_libdir}/pgsql/fuzzystrmatch.so
%{_libdir}/pgsql/hstore.so
%{_libdir}/pgsql/hstore_plpython3.so
%{_libdir}/pgsql/insert_username.so
%{_libdir}/pgsql/isn.so
%{_libdir}/pgsql/jsonb_plpython3.so
%{_libdir}/pgsql/lo.so
%{_libdir}/pgsql/ltree.so
%{_libdir}/pgsql/ltree_plpython3.so
%{_libdir}/pgsql/pg_logicalinspect.so
%{_libdir}/pgsql/pg_overexplain.so
%{_libdir}/pgsql/moddatetime.so
%{_libdir}/pgsql/pageinspect.so
%{_libdir}/pgsql/passwordcheck.so
%{_libdir}/pgsql/pg_buffercache.so
%{_libdir}/pgsql/pg_freespacemap.so
%{_libdir}/pgsql/pg_prewarm.so
%{_libdir}/pgsql/pg_stat_statements.so
%{_libdir}/pgsql/pg_surgery.so
%{_libdir}/pgsql/pg_trgm.so
%{_libdir}/pgsql/pg_visibility.so
%{_libdir}/pgsql/pg_walinspect.so
%{_libdir}/pgsql/basic_archive.so
%{_libdir}/pgsql/basebackup_to_shell.so
%{_libdir}/pgsql/pgcrypto.so
%{_libdir}/pgsql/pgrowlocks.so
%{_libdir}/pgsql/pgstattuple.so
%{_libdir}/pgsql/postgres_fdw.so
%{_libdir}/pgsql/refint.so
%{_libdir}/pgsql/seg.so
%{_libdir}/pgsql/tablefunc.so
%{_libdir}/pgsql/tcn.so
%{_libdir}/pgsql/test_decoding.so
%{_libdir}/pgsql/tsm_system_rows.so
%{_libdir}/pgsql/tsm_system_time.so
%{_libdir}/pgsql/unaccent.so
%{_datadir}/pgsql/contrib/sepgsql.sql
%{_libdir}/pgsql/sepgsql.so
%{_datadir}/pgsql/extension/sslinfo*
%{_libdir}/pgsql/sslinfo.so
%{_datadir}/pgsql/extension/uuid-ossp*
%{_libdir}/pgsql/uuid-ossp.so
%{_datadir}/pgsql/extension/xml2*
%{_libdir}/pgsql/pgxml.so

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
%dir %{_datadir}/pgsql
%{_datadir}/pgsql/*.sample
%dir %{_datadir}/pgsql/contrib
%dir %{_datadir}/pgsql/extension
%{_datadir}/pgsql/extension/plpgsql*
%{_datadir}/pgsql/information_schema.sql
%{_datadir}/pgsql/postgres.bki
%{_datadir}/pgsql/snowball_create.sql
%{_datadir}/pgsql/sql_features.txt
%{_datadir}/pgsql/system_constraints.sql
%{_datadir}/pgsql/system_functions.sql
%{_datadir}/pgsql/system_views.sql
%{_datadir}/pgsql/timezonesets/
%{_datadir}/pgsql/tsearch_data/
%dir %{_libdir}/pgsql
%{_libdir}/pgsql/*_and_*.so
%{_libdir}/pgsql/dict_snowball.so
%{_libdir}/pgsql/euc2004_sjis2004.so
%{_libdir}/pgsql/libpqwalreceiver.so
%{_libdir}/pgsql/pgoutput.so
%{_libdir}/pgsql/plpgsql.so

%attr(700,postgres,postgres) %dir %{?_localstatedir}/lib/pgsql
%attr(644,postgres,postgres) %config(noreplace) %{?_localstatedir}/lib/pgsql/.bash_profile
%attr(700,postgres,postgres) %dir %{?_localstatedir}/lib/pgsql/backups
%attr(700,postgres,postgres) %dir %{?_localstatedir}/lib/pgsql/data
%ghost %attr(755,postgres,postgres) %dir %{_rundir}/postgresql
%config(noreplace) /etc/pam.d/postgresql
%{_sysusersdir}/postgresql.conf
%{_tmpfilesdir}/postgresql.conf
%{_unitdir}/postgresql.service

%files server-devel -f devel.lst
%{_bindir}/pg_config
%dir %{_datadir}/pgsql
%{_datadir}/pgsql/errcodes.txt
%dir %{_includedir}/pgsql
%{_includedir}/pgsql/server
%{_libdir}/pgsql/pgxs/

%files devel
%{_bindir}/pg_config
%{_includedir}/libpq-events.h
%{_includedir}/libpq-fe.h
%{_includedir}/postgres_ext.h
%{_includedir}/pgsql/internal/*.h
%{_includedir}/pgsql/internal/libpq/pqcomm.h

%{_includedir}/pgsql/internal/libpq/protocol.h

%{_includedir}/libpq/*.h
%{_libdir}/pkgconfig/libpq.pc
%{_libdir}/libpq.so
%{_includedir}/pg_config*.h

%files plpython3 -f plpython3.lst
%{_datadir}/pgsql/extension/plpython3*
%{_libdir}/pgsql/plpython3.so

%if %{with test}
%files test
%attr(-,postgres,postgres) %{_libdir}/pgsql/test
%endif

%changelog
%autochangelog
