# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Mroonga and RocksDB are available only for x86_64 architecture
# see https://mariadb.com/kb/en/mariadb/about-mroonga/ and
# https://mariadb.com/kb/en/library/myrocks-supported-platforms/
%ifarch x86_64
%define with_mroonga 1
%define with_rocksdb 1
%else
%define with_mroonga 0
%define with_rocksdb 0
%endif

# Define python interpreter version
%define python_path %{_bindir}/python3
# Source directory (for declarative builds where install runs from build dir)
%define srcdir %{_builddir}/%{name}-%{version}

Name:           mariadb
Version:        11.8.6
Release:        %autorelease
Summary:        Server part of MariaDB
License:        GPL-2.0-only
URL:            https://www.mariadb.org
VCS:            git:https://github.com/MariaDB/server.git
#!RemoteAsset
Source:         https://archive.mariadb.org/%{name}-%{version}/source/%{name}-%{version}.tar.gz
Source1:        mysql-user.sysusers
Source2:        my.ini
Source3:        mariadb.service.in
Source4:        mariadb.target
Source5:        mysql-systemd-helper
Source6:        mariadb@.service.in
Source7:        mariadb.tmpfiles
BuildSystem:    cmake

Patch0:         fix-pamdir.patch

BuildOption(conf):  -DWITH_SSL=system
BuildOption(conf):  -DENABLED_PROFILING=ON
BuildOption(conf):  -DENABLE_DEBUG_SYNC=OFF
BuildOption(conf):  -DWITH_PIC=ON
BuildOption(conf):  -DWITH_ZLIB=system
BuildOption(conf):  -DWITH_JEMALLOC=no
BuildOption(conf):  -DWITH_READLINE=OFF
BuildOption(conf):  -DINSTALL_LAYOUT=RPM
BuildOption(conf):  -DINSTALL_SBINDIR="$(basename %{_sbindir})"
BuildOption(conf):  -DWITH_LZ4=system
BuildOption(conf):  -DMYSQL_UNIX_ADDR="%{_rundir}/mysql/mysql.sock"
BuildOption(conf):  -DINSTALL_UNIX_ADDRDIR="%{_rundir}/mysql/mysql.sock"
BuildOption(conf):  -DINSTALL_MYSQLSHAREDIR=share/%{name}
BuildOption(conf):  -DWITH_COMMENT="MariaDB rpm"
BuildOption(conf):  -DWITH_EXTRA_CHARSET=all
BuildOption(conf):  -DWITH_INNOBASE_STORAGE_ENGINE=1
BuildOption(conf):  -DWITH_PERFSCHEMA_STORAGE_ENGINE=1
BuildOption(conf):  -DWITH_LIBWRAP=OFF
BuildOption(conf):  -DPLUGIN_OQGRAPH=NO
%if 0%{with_mroonga} < 1
BuildOption(conf):  -DPLUGIN_MROONGA=NO
%endif
%if 0%{with_rocksdb} < 1
BuildOption(conf):  -DPLUGIN_ROCKSDB=NO
%endif
BuildOption(conf):  -DPYTHON_SHEBANG=%{python_path}
BuildOption(conf):  -DWITH_EMBEDDED_SERVER=true
BuildOption(conf):  -DWITH_MARIABACKUP=ON
BuildOption(conf):  -DCOMPILATION_COMMENT="MariaDB package"
BuildOption(conf):  -DENABLE_DOWNLOADS=false
BuildOption(conf):  -DWITH_FMT=system
BuildOption(conf):  -DINSTALL_PLUGINDIR_RPM="%{_lib}/mysql/plugin"
BuildOption(conf):  -DINSTALL_LIBDIR_RPM="%{_lib}"
BuildOption(conf):  -DINSTALL_SYSCONF2DIR="%{_sysconfdir}/my.cnf.d"
BuildOption(conf):  -DINSTALL_SQLBENCHDIR=share
BuildOption(conf):  -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now -Wl,-Bsymbolic -Wl,-Bsymbolic-functions"
BuildOption(conf):  -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now -Wl,-Bsymbolic -Wl,-Bsymbolic-functions"
BuildOption(conf):  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now -Wl,-Bsymbolic -Wl,-Bsymbolic-functions"
BuildOption(conf):  -Wno-dev
BuildOption(check):  -E test-connect

# needed for bison SQL parser and wsrep API
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(fmt)
# GSSAPI
BuildRequires:  pkgconfig(krb5-gssapi)
# embedded server libmariadbd
BuildRequires:  pkgconfig(libaio)
# mariabackup tool
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(bzip2)
# commands history feature
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libxml-2.0)
# CLI graphic and wsrep API
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
# auth_pam.so plugin
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(lzo2)

# Required by rcmysql
Requires:       %{name}-client
Requires:       %{name}-errormessages = %{version}-%{release}
Requires:       hostname
Requires:       perl
# myrocks_hotbackup needs MySQLdb - if we want to use it under python3, we need python3-mysqlclient
# Requires:       python3-mysqlclient


%description
MariaDB is an open-source, multi-threaded, relational database management
system. It's a backward compatible, drop-in replacement branch of the
MySQL Community Server.

This package only contains the server-side programs.

%package        libs
Summary:        MariaDB embedded server library
Requires:       %{name}-errormessages >= %{version}-%{release}

%description    libs
This package contains MariaDB library that allows to run an embedded
MariaDB server inside a client application.

%package        devel
Summary:        MariaDB embedded server development files
Requires:       pkgconfig(libaio)
Requires:       pkgconfig(libmariadb)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains the development header files and libraries
for developing applications that embed the MariaDB.

%package        client
Summary:        Client for MariaDB
Requires:       %{name}-errormessages = %{version}-%{release}

%description    client
This package contains the standard clients for MariaDB.

%package        errormessages
Summary:        The error messages files required by server, client and libmariadbd
BuildArch:      noarch

%description    errormessages
This package provides translated error messages for the standalone
server daemon, embedded server and client.

%package        bench
Summary:        Benchmarks for MariaDB
Requires:       %{name}-client
# Requires:       perl-DBD-mysql

%description    bench
This package contains benchmark scripts and data for MariaDB.

To run these database benchmarks, start the script "run-all-tests" in
the directory %{_datadir}/sql-bench after starting MariaDB.

%package        test
Summary:        Testsuite for MariaDB
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-bench = %{version}-%{release}
Requires:       %{name}-client = %{version}-%{release}
Requires:       %{name}-tools = %{version}-%{release}
# Requires libmariadb_plugins in order to test client plugins successfuly
# Requires:       libmariadb_plugins >= 3.0
# Requires:       perl-DBD-mysql
Requires:       procps
Requires:       time
# Tests requires time and ps and some perl modules
Requires:       perl(Data::Dumper)
Requires:       perl(Env)
Requires:       perl(Exporter)
Requires:       perl(Fcntl)
Requires:       perl(File::Temp)
Requires:       perl(Getopt::Long)
Requires:       perl(IPC::Open3)
Requires:       perl(Memoize)
Requires:       perl(Socket)
Requires:       perl(Symbol)
Requires:       perl(Sys::Hostname)
Requires:       perl(Test::More)
Requires:       perl(Time::HiRes)

%description    test
This package contains the test scripts and data for MariaDB.

%package        tools
Summary:        MariaDB tools
# Requires:       perl-DBD-mysql

%description    tools
A set of scripts for administering a MariaDB or developing
applications with MariaDB.

%prep -a
# Remove JAR files from the tarball (used for testing from the source)
find . -name "*.jar" -type f -exec rm --verbose -f {} \;

# Remove unneeded manpages ('make install' basically installs everything under
# man/*)
rm -f man/mysqlman.1        # dummy fallback manpage
[ \! -f man/CMakeLists.txt ] || sed -i 's|mysqlman.1||'     man/CMakeLists.txt
rm -f man/mysql.server.1    # init script, not installed in our rpm
[ \! -f man/CMakeLists.txt ] || sed -i 's|mysql.server.1||' man/CMakeLists.txt
rm -f man/make_win_*.1      # windows build scripts
rm -f man/comp_err.1        # built-time utility

# Breaks VPATH builds when in sourcedir, is generated in the builddirs
rm -f sql/sql_builtin.cc

# Broken test that needs sources
rm -f %{name}-test/t/file_contents.test %{name}-test/r/file_contents.result

# Specify perl path on shebangs
for i in `grep -Rl '^#!%{_bindir}/env perl$' .`; do
    sed -i 's|%{_bindir}/env perl|%{_bindir}/perl|' $i
done

%install -a
# Helper function to generate filelist for binaries and their manpages
filelist()
{
    echo '%%defattr(-, root, root)'
    pushd %{buildroot} >/dev/null
    for i; do
        if test -e usr/sbin/"$i"; then
            echo %{_sbindir}/"$i"
        fi
        if test -e usr/bin/"$i"; then
            echo %{_bindir}/"$i"
        fi
        if test -d usr/share/*/"$i"; then
            echo "/`echo usr/share/*/"$i"`"
        fi
        if test -n "`ls -1 %{buildroot}$i 2> /dev/null`"; then
            echo "$i"
        fi
        if ls usr/share/man/*/"$i".[1-9]* >/dev/null 2>&1; then
            echo "%{_mandir}/*/$i.[1-9]*"
        fi
    done
    popd >/dev/null
}

# Create log directory with the expected perms of mysql
install -d -m 700 %{buildroot}%{_localstatedir}/log/mysql/

# Remove static libs (FIXME: don't build them at all...)
rm %{buildroot}%{_libdir}/*.a

# Remove unused stuff
rm -f %{buildroot}%{_datadir}/mysql/{errmsg-utf8.txt,mysql-log-rotate}
rm -f %{buildroot}%{_libdir}/mysql/plugin/daemon_example.ini
# binary-configure creates the MySQL system tables and starts the server (not used)
rm -f %{buildroot}%{_datadir}/%{name}/binary-configure
# FS files first-bytes recoginiton (not updated by upstream since nobody realy use that)
rm -f %{buildroot}%{_datadir}/%{name}/magic
# Upstream ships them because of MDEV-10797 (we don't need them as we use our own systemd scripts)
rm -f %{buildroot}%{_datadir}/%{name}/mysql.server
rm -f %{buildroot}%{_datadir}/%{name}/mysqld_multi.server
# upstream installs links for mysql
unlink %{buildroot}%{_datadir}/%{name}/systemd/mysql.service
unlink %{buildroot}%{_datadir}/%{name}/systemd/mysqld.service
unlink %{buildroot}%{_unitdir}/mysqld.service
# The old fork of mytop utility (we ship it as a separate package)
rm -f %{buildroot}%{_bindir}/mytop
# xtrabackup is not supported for MariaDB >= 10.3
rm -f %{buildroot}%{_bindir}/wsrep_sst_xtrabackup-v2
rm -f %{buildroot}%{_bindir}/wsrep_sst_xtrabackup

# Remove all wsrep/galera related files (we don't provide galera subpackage)
rm -f %{buildroot}%{_bindir}/galera_new_cluster
rm -f %{buildroot}%{_bindir}/galera_recovery
rm -f %{buildroot}%{_bindir}/wsrep_sst_backup
rm -f %{buildroot}%{_bindir}/wsrep_sst_common
rm -f %{buildroot}%{_bindir}/wsrep_sst_mariabackup
rm -f %{buildroot}%{_bindir}/wsrep_sst_mysqldump
rm -f %{buildroot}%{_bindir}/wsrep_sst_rsync
rm -f %{buildroot}%{_bindir}/wsrep_sst_rsync_wan
rm -f %{buildroot}%{_mandir}/man1/galera_new_cluster.1*
rm -f %{buildroot}%{_mandir}/man1/galera_recovery.1*
rm -f %{buildroot}%{_mandir}/man1/wsrep_sst_backup.1*
rm -f %{buildroot}%{_mandir}/man1/wsrep_sst_common.1*
rm -f %{buildroot}%{_mandir}/man1/wsrep_sst_mariabackup.1*
rm -f %{buildroot}%{_mandir}/man1/wsrep_sst_mysqldump.1*
rm -f %{buildroot}%{_mandir}/man1/wsrep_sst_rsync.1*
rm -f %{buildroot}%{_mandir}/man1/wsrep_sst_rsync_wan.1*
rm -f %{buildroot}%{_datadir}/%{name}/systemd/use_galera_new_cluster.conf
rm -f %{buildroot}%{_datadir}/%{name}/wsrep_notify
# Remove mysql.service symlink (we use mariadb.service instead)
rm -f %{buildroot}%{_unitdir}/mysql.service

# Remove unused upstream services
rm -f %{buildroot}'%{_unitdir}/mariadb.service'
rm -f %{buildroot}'%{_unitdir}/mariadb@.service'
rm -f %{buildroot}'%{_unitdir}/mariadb@bootstrap.service.d/use_galera_new_cluster.conf'

# Remove systemd-sysusers conf file for creating of mysql user (we do it in the specfile)
rm -f %{buildroot}%{_sysusersdir}/mariadb.conf

# Remove client libraries that are now provided in mariadb-connector-c
# Client library and links
rm %{buildroot}%{_libdir}/libmariadb.so.*
unlink %{buildroot}%{_libdir}/libmysqlclient.so
unlink %{buildroot}%{_libdir}/libmysqlclient_r.so
unlink %{buildroot}%{_libdir}/libmariadb.so
# Client plugins
rm %{buildroot}%{_libdir}/mysql/plugin/{auth_gssapi_client.so,dialog.so,mysql_clear_password.so,sha256_password.so,caching_sha2_password.so,client_ed25519.so}
# Devel files
rm %{buildroot}%{_bindir}/mysql_config
rm %{buildroot}%{_bindir}/mariadb_config
rm %{buildroot}%{_bindir}/mariadb-config
rm %{buildroot}%{_libdir}/pkgconfig/mariadb.pc
rm -f %{buildroot}%{_prefix}/lib/pkgconfig/libmariadb.pc
rm -f %{buildroot}%{_libdir}/pkgconfig/libmariadb.pc
rm %{buildroot}%{_datadir}/aclocal/mysql.m4
rm %{buildroot}%{_mandir}/man1/mariadb_config*.1*
rm %{buildroot}%{_mandir}/man1/mysql_config*.1*
rm %{buildroot}%{_mandir}/man1/mytop.1*
rm -r %{buildroot}%{_includedir}/mysql
# Devel man pages
rm -rf %{buildroot}%{_mandir}/man3/*

# Rename the wsrep README so it corresponds with the other README names
cp %{srcdir}/Docs/README-wsrep %{srcdir}/Docs/README.wsrep

# Generate various filelists (binaries and manpages)
# mariadb.files
filelist mariabackup mariadb-backup mbstream innochecksum mariadb-service-convert my_print_defaults myisam_ftdump myisamchk myisamlog myisampack mysql_fix_extensions mariadb-fix-extensions mysql_install_db mariadb-install-db mysql_secure_installation mariadb-secure-installation mysql_upgrade mariadb-upgrade mysqld mariadbd mysqld_multi mariadbd-multi mysqld_safe mariadbd-safe mysqlbinlog mariadb-binlog mysqldumpslow mariadb-dumpslow resolve_stack_dump resolveip {m,}aria_chk {m,}aria_dump_log {m,}aria_ftdump {m,}aria_pack {m,}aria_read_log tokuft_logprint tokuft_logdump tokuftdump mysql_ldb mariadb-ldb sst_dump myrocks_hotbackup >mariadb.files

# mariadb-client.files
filelist mysql mariadb mysqladmin mariadb-admin mysqlcheck mariadb-check mysqldump mariadb-dump mysqlimport mariadb-import mysqlshow mariadb-show mysql_config_editor mysqld_safe_helper mariadbd-safe-helper >mariadb-client.files

# Mysql has configuration file in _bindir
if [ -f %{srcdir}/scripts/mysqlaccess.conf ] ; then
    install -m 640 %{srcdir}/scripts/mysqlaccess.conf %{buildroot}%{_sysconfdir}/mysqlaccess.conf
    rm -f %{buildroot}%{_bindir}/mysqlaccess.conf
    echo '%config(noreplace) %attr(0640, root, mysql) %{_sysconfdir}/mysqlaccess.conf' >> mariadb-client.files
fi


# mariadb-bench.files
filelist mysqlslap mariadb-slap >mariadb-bench.files

# mariadb-test.files
filelist mysql_client_test mariadb-client-test mysql_client_test_embedded mariadb-client-test-embedded mysql_waitpid mariadb-waitpid mysqltest mariadb-test mysqltest_embedded mariadb-test-embedded >mariadb-test.files

# mariadb-tools.files
filelist msql2mysql mysql_plugin mariadb-plugin mysql_convert_table_format mariadb-convert-table-format mysql_find_rows mariadb-find-rows mysql_setpermission mariadb-setpermission mysql_tzinfo_to_sql mariadb-tzinfo-to-sql mysqlaccess mariadb-access mysqlhotcopy mariadb-hotcopy perror replace mysql_embedded mariadb-embedded aria_s3_copy mariadb-conv >mariadb-tools.files

# All configuration files
echo '%{_datadir}/%{name}/*.cnf' >> mariadb.files

# Special errormessages approach
echo '%%defattr(-, root, root)' > %{_builddir}/errormessages.files
pushd %{buildroot} >/dev/null
for f in usr/share/%{name}/*; do
    if test -e $f/errmsg.sys; then
        echo "%%dir /$f" >> %{_builddir}/errormessages.files
    fi
done
popd >/dev/null
mv %{_builddir}/errormessages.files mariadb-errormessages.files

# Files not installed by make install
# Some of the documentation we need to have installed
DOCS=(COPYING README.md plugin/daemon_example/daemon_example.ini)
DOCDIR=%{buildroot}%{_defaultdocdir}/%{name}
install -d -m 755 ${DOCDIR}
for i in "${DOCS[@]}"; do
    install -m 644 "%{srcdir}/${i}" "${DOCDIR}" || true
done

# Install default configuration file
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/my.cnf

# Systemd/initscript
install -D -m 755 %{_sourcedir}/mysql-systemd-helper '%{buildroot}'%{_libexecdir}/mysql/mysql-systemd-helper
sed -i 's|@MYSQLVER@|%{version}|' '%{buildroot}'%{_libexecdir}/mysql/mysql-systemd-helper
ln -sf service '%{buildroot}'%{_sbindir}/rcmysql
ln -sf service '%{buildroot}'%{_sbindir}/rcmariadb
rm -rf '%{buildroot}'%{_sysconfdir}/init.d
sed "s|@LIBEXECDIR@|%{_libexecdir}|g" %{_sourcedir}/mariadb.service.in > '%{buildroot}'%{_unitdir}/mariadb.service
sed "s|@LIBEXECDIR@|%{_libexecdir}|g" %{_sourcedir}/mariadb@.service.in > '%{buildroot}'%{_unitdir}/mariadb@.service
install -D -m 644 %{_sourcedir}/mariadb.target '%{buildroot}'%{_unitdir}/mariadb.target
# Aliases for the backward compatibility. Create symlinks from the alias to the existing one
# We can't use 'Alias=' option only because it's effective only when the unit is enabled

# Replace the default socket for multi instance mariadb with the one used by
# mysql-systemd-helper
sed -e 's:mysql.sock-%I:mysql.%I.sock:' -i %{buildroot}%{_unitdir}/mariadb@.socket

# Tmpfiles config for /run/mysql socket directory and temp file exclusion
install -m0644 -D %{SOURCE7} %{buildroot}%{_tmpfilesdir}/mariadb.conf

# Testsuite
install -d -m 755 '%{buildroot}'%{_datadir}/%{name}-test/
mkdir '%{buildroot}'%{_datadir}/%{name}-test%{_localstatedir}

# Install the list of skipped tests to be available for user runs
# Use srcdir because declarative build runs install from build directory
if [ -f %{srcdir}/mysql-test/unstable-tests ]; then
    install -p -m 0644 %{srcdir}/mysql-test/unstable-tests %{buildroot}%{_datadir}/%{name}-test
fi

# Final fixes
find '%{buildroot}'%{_datadir}/%{name}-test -name '*.orig' -delete
%fdupes -s '%{buildroot}'%{_datadir}/%{name}-test
for i in `grep -Rl '\r' '%{buildroot}'%{_datadir}/sql-bench`; do
    dos2unix "$i"
done

# Use our configuration stuff instead of upstream one
rm -rf '%{buildroot}'%{_sysconfdir}/my.cnf.d
install -d -m 755 '%{buildroot}'%{_sysconfdir}/my.cnf.d

# Documentation that was copied to wrong folder
rm -f '%{buildroot}'%{_datadir}/doc/* 2> /dev/null || true

# Unwanted packaged stuff
rm -rf '%{buildroot}'%{_datadir}/mysql/{solaris,SELinux}

# Create the directory specified in 'secure-file-priv' option
mkdir -p '%{buildroot}'%{_localstatedir}/lib/mysql-files

# Install sysusers.d file
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/mysql-user.conf

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%systemd_post mariadb.service mariadb@.service mariadb.socket mariadb-extra.socket mariadb.target

chmod 4755 %{_libdir}/mysql/plugin/auth_pam_tool_dir/auth_pam_tool 2>/dev/null || :

%preun
%systemd_preun mariadb.service mariadb.socket mariadb-extra.socket mariadb.target

%postun
%systemd_postun mariadb.service mariadb.socket mariadb-extra.socket mariadb.target

%files -f mariadb.files
%config(noreplace) %attr(-, root, mysql) %{_sysconfdir}/my.cnf
%config(noreplace) %attr(-, root, mysql) %{_sysconfdir}/my.cnf.d/
%config(noreplace) %{_pam_secconfdir}/user_map.conf
%config %{_sysconfdir}/logrotate.d/%{name}
%{_datadir}/%{name}/%{name}.logrotate
%doc %{_defaultdocdir}/%{name}
%dir %{_libexecdir}/mysql
%dir %attr(0700, mysql, mysql) %{_localstatedir}/log/mysql
%{_libexecdir}/mysql/mysql-systemd-helper
%{_unitdir}/mariadb.service
%{_unitdir}/mariadb@.service
%{_unitdir}/mariadb.target
%{_unitdir}/mariadb-extra.socket
%{_unitdir}/mariadb-extra@.socket
%{_unitdir}/mariadb.socket
%{_unitdir}/mariadb@.socket
%{_tmpfilesdir}/mariadb.conf
%{_sysusersdir}/mysql-user.conf
%{_sbindir}/rcmysql
%{_sbindir}/rcmariadb
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/charsets/
%{_datadir}/%{name}/*.sql
%dir %{_libdir}/mysql
%dir %{_libdir}/mysql/plugin
%{_libdir}/mysql/plugin/*.so
%exclude %{_libdir}/mysql/plugin/dialog*.so
%{_pam_moduledir}/pam_user_map.so
%dir %attr(0750, root, mysql) %{_libdir}/mysql/plugin/auth_pam_tool_dir
%verify(not mode) %attr(4755,root,root) %{_libdir}/mysql/plugin/auth_pam_tool_dir/auth_pam_tool
%dir %attr(0750, mysql, mysql) %{_localstatedir}/lib/mysql-files
%if 0%{with_mroonga} > 0
%{_datadir}/mariadb/mroonga/
%dir %{_datadir}/groonga/
%{_datadir}/groonga/COPYING
%{_datadir}/groonga/README.md
%dir %{_datadir}/groonga-normalizer-mysql
%{_datadir}/groonga-normalizer-mysql/README.md
%{_datadir}/groonga-normalizer-mysql/lgpl-2.0.txt
%endif
%dir %{_datadir}/%{name}/policy
%dir %{_datadir}/%{name}/policy/apparmor
%{_datadir}/%{name}/policy/apparmor/README
%{_datadir}/%{name}/policy/apparmor/usr.sbin.mysqld*
%dir %{_datadir}/%{name}/policy/selinux
%{_datadir}/%{name}/policy/selinux/README
%{_datadir}/%{name}/policy/selinux/mariadb-server.*
%{_datadir}/%{name}/policy/selinux/mariadb.te
%dir %{_datadir}/%{name}/systemd
%{_datadir}/%{name}/systemd/mariadb.service
%{_datadir}/%{name}/systemd/mariadb@.service
%{_datadir}/%{name}/systemd/mariadb-extra@.socket
%{_datadir}/%{name}/systemd/mariadb@.socket

%files libs
%{_libdir}/libmariadbd.so.*

%files devel
%{_libdir}/libmysqld.so
%{_libdir}/libmariadbd.so

%files client -f mariadb-client.files
%dir %{_libdir}/mysql
%dir %{_libdir}/mysql/plugin
%{_libdir}/mysql/plugin/dialog_examples.so

%files errormessages -f mariadb-errormessages.files
%{_datadir}/%{name}/*/errmsg.sys

%files bench -f mariadb-bench.files
%{_datadir}/sql-bench
%{_datadir}/%{name}/mini-benchmark

%files test -f mariadb-test.files
%{_bindir}/test-connect-t
%{_mandir}/man1/my_safe_process.1%{?ext_man}
%{_mandir}/man1/mysql-test-run.pl.1%{?ext_man}
%{_mandir}/man1/mysql-stress-test.pl.1%{?ext_man}
%{_datadir}/%{name}-test/valgrind.supp
%dir %attr(755, mysql, mysql) %{_datadir}/%{name}-test
%attr(-, mysql, mysql) %{_datadir}/%{name}-test/[^v]*
%dir %attr(755, mysql, mysql) %{_datadir}/%{name}-test%{_localstatedir}

%files tools -f mariadb-tools.files

%changelog
%autochangelog
