# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Set 1 to enable
%bcond tcl 0

Name:           db
Version:        6.2.32
Release:        %autorelease
Summary:        The Berkeley DB database library for C
License:        BSD-3-Clause AND LGPL-2.1-only AND Sleepycat
URL:            https://www.oracle.com/database/berkeley-db/
# This package does not have a VCS link
#!RemoteAsset
Source0:        https://download.oracle.com/berkeley-db/db-%{version}.tar.gz
# I really don't want to use autotools here

BuildRequires:  make
BuildRequires:  config
BuildRequires:  libtool
BuildRequires:  chrpath
BuildRequires:  pkgconfig(zlib)
BuildRequires:  gdbm-devel
BuildRequires:  pkgconfig(lmdb)

%description
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. The Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching, and database
recovery. The Berkeley DB supports C, C++, and Perl APIs. It is
used by many applications, including Python and Perl, so this should
be installed on all systems.

%package        utils
Summary:        Command line tools for managing Berkeley DB databases
Requires:       %{name} = %{version}-%{release}

%description    utils
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching, and database
recovery. DB supports C, C++ and Perl APIs.

%package        devel
Summary:        C development files for the Berkeley DB library
Requires:       %{name} = %{version}-%{release}

%description    devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. This package contains the header files,
libraries, and documentation for building programs which use the
Berkeley DB.

%prep
%autosetup -n db-%{version}
cd dist
./s_config



%conf
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -std=gnu99 -pthread"
export CXXFLAGS="$RPM_OPT_FLAGS -g -pthread"
export LDFLAGS="${LDFLAGS:+$LDFLAGS }-pthread"
export LIBS="${LIBS:+$LIBS }-lpthread"
install $(command -v config.guess) %{_builddir}/db-%{version}/dist/config.guess
install -m 755 $(command -v config.sub) %{_builddir}/db-%{version}/dist/config.sub
install $(command -v config.guess) %{_builddir}/db-%{version}/lang/sql/sqlite/config.guess
install -m 755 $(command -v config.sub) %{_builddir}/db-%{version}/lang/sql/sqlite/config.sub
pushd build_unix
%define _configure ../dist/configure
%configure -C \
    --with-mutex=POSIX/pthreads \
    --enable-compat185 \
    --disable-dump185 \
    --enable-shared \
    --disable-static \
%if %{with tcl}
    --enable-tcl --with-tcl=/usr/%{_lib} TCLSH_CMD=$(which tclsh%{__tclversion}) \
%endif
    --enable-cxx \
    --enable-sql \
    --disable-rpath
popd

%build
pushd build_unix
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -std=gnu99"
%make_build
popd

%install
%make_install STRIP=/bin/true -C build_unix
# These sucks
rm -f %{buildroot}%{_libdir}/{libdb.a,libdb_cxx.a,libdb_tcl.a,libdb_sql.a}
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la
rm -rf docs/csharp
rm -rf examples/csharp
rm -rf docs/installation
# Don't need these docs
rm -rf ${RPM_BUILD_ROOT}%{_prefix}/docs
# Ensure shared libraries are executable
chmod +x %{buildroot}%{_libdir}/*.so*
# Move the header files to a subdirectory
mkdir -p %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/%{name}/
# Create symlinks to includes
for i in db.h db_cxx.h db_185.h; do
 ln -s %{name}/$i %{buildroot}%{_includedir}
done
# Avoid Permission denied
chmod u+w %{buildroot}%{_bindir} ${RPM_BUILD_ROOT}%{_bindir}/*
# remove rpath
chrpath -d %{buildroot}%{_libdir}/*.so ${RPM_BUILD_ROOT}%{_bindir}/*
# unify documentation and examples
mv examples docs

# no tests
%check


%files
%license LICENSE
%doc README
%{_libdir}/libdb-*.so

%files devel
%doc docs/*
%{_bindir}/dbsql
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/db.h
%{_includedir}/%{name}/db_185.h
%{_includedir}/db.h
%{_includedir}/db_185.h
%{_includedir}/%{name}/db_cxx.h
%{_includedir}/db_cxx.h
%{_includedir}/%{name}/dbsql.h
%{_libdir}/libdb.so
%if %{with tcl}
%{_libdir}/libdb_tcl.so
%{_libdir}/libdb_tcl-*.so
%endif
%{_libdir}/libdb_sql.so
%{_libdir}/libdb_sql-*.so
%{_libdir}/libdb_cxx.so
%{_libdir}/libdb_cxx-*.so

%files utils
%{_bindir}/db*_convert
%{_bindir}/db*_archive
%{_bindir}/db*_checkpoint
%{_bindir}/db*_deadlock
%{_bindir}/db*_dump*
%{_bindir}/db*_hotbackup
%{_bindir}/db*_load
%{_bindir}/db*_printlog
%{_bindir}/db*_recover
%{_bindir}/db*_replicate
%{_bindir}/db*_stat
%{_bindir}/db*_upgrade
%{_bindir}/db*_verify
%{_bindir}/db*_tuner

%changelog
%{?autochangelog}
