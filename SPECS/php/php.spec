# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zephyr Du <zhonghang.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# From: https://gitlab.archlinux.org/archlinux/packaging/packages/php/-/blob/main/PKGBUILD
#     > LTO is incompatible with global registers and results in reduced performance:
#     > https://gitlab.archlinux.org/archlinux/packaging/packages/php/-/merge_requests/3
%global _lto_cflags %{nil}

%global _test_target test

Name:           php
Version:        8.5.5
Release:        %autorelease
Summary:        The PHP Interpreter
License:        PHP-3.01
URL:            https://www.php.net
VCS:            git:https://github.com/php/php-src
#!RemoteAsset:  sha256:276279f637a875a514346b332bba6d8b06c036cf7979a858e5c55f72c4874884
Source0:        https://www.php.net/distributions/%{name}-%{version}.tar.gz
# Upstream fix for expired SNI certificates in bug74796 and bug80770 tests.
# This patch will merge in future version
Patch0001:         0001-Fix-SNI-tests-for-bugs-80770-and-74796.patch
BuildSystem:    autotools

BuildOption(conf):  --enable-re2c-cgoto
BuildOption(conf):  --with-config-file-path=%{_sysconfdir}/php
BuildOption(conf):  --with-config-file-scan-dir=%{_sysconfdir}/php/conf.d
BuildOption(conf):  --with-curl=shared
BuildOption(conf):  --enable-gd=shared
BuildOption(conf):  --with-freetype
BuildOption(conf):  --with-jpeg
BuildOption(conf):  --with-openssl=shared
BuildOption(conf):  --enable-pcntl=shared
BuildOption(conf):  --with-zip=shared
BuildOption(conf):  --with-zlib=shared
BuildOption(conf):  EXTENSION_DIR=%{_libdir}/php/extensions
BuildOption(build):  CFLAGS="$RPM_OPT_FLAGS"
BuildOption(build):  LDFLAGS="$RPM_LD_FLAGS"
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  INSTALL_ROOT=%{buildroot}
BuildOption(install):  bindir=%{_bindir}
BuildOption(install):  sbindir=%{_sbindir}
BuildOption(install):  libdir=%{_libdir}
BuildOption(check):  REPORT_EXIT_STATUS=1
BuildOption(check):  NO_INTERACTION=1
BuildOption(check):  SKIP_ONLINE_TESTS=1
BuildOption(check):  SKIP_SLOW_TESTS=1
BuildOption(check):  TESTS="-r php-test-list"

BuildRequires:  re2c
BuildRequires:  bison
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
PHP is a popular general-purpose scripting language that is especially suited
to web development. Fast, flexible and pragmatic, PHP powers everything from
your blog to the most popular websites in the world.

%package        devel
Summary:        Files for developing with php
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Includes and definitions for developing with php.

%package        curl
Summary:        PHP libcurl integration
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    curl
This package provides the PHP extension for libcurl.

%package        gd
Summary:        PHP GD graphics extension
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gd
This package provides the PHP extension for creating and manipulating images
using the GD graphics library.

%package        openssl
Summary:        PHP OpenSSL integration
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    openssl
This package provides the PHP extension for OpenSSL cryptography and TLS
stream support.

%package        pcntl
Summary:        PHP process control extension
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    pcntl
This package provides the PHP extension for Unix process control functions.

%package        zip
Summary:        PHP ZIP archive extension
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    zip
This package provides the PHP extension for reading and writing ZIP archives.

%package        zlib
Summary:        PHP zlib compression extension
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    zlib
This package provides the PHP extension for zlib compression support.

%check -p
# These tests can't run on OBS worker, disabled
find . -type f -name '*.phpt' \
    ! -path './ext/curl/tests/curl_setopt_ssl.phpt' \
    ! -path './ext/opcache/tests/bug78185.phpt' \
    ! -path './ext/opcache/tests/gh16979_check_file_cache_function.phpt' \
    ! -path './ext/openssl/tests/sni_server.phpt' \
    ! -path './ext/openssl/tests/sni_server_key_cert.phpt' \
    ! -path './ext/pcntl/tests/pcntl_cpuaffinity.phpt' \
    ! -path './ext/pcntl/tests/pcntl_getcpu.phpt' \
    ! -path './ext/pdo_pgsql/tests/transations_deprecations.phpt' \
    | sort > php-test-list

%install -a
install -D -m644 "php.ini-production" "%{buildroot}/etc/php/php.ini"
install -d -m755 "%{buildroot}/etc/php/conf.d/"
for ext in curl gd openssl pcntl zip zlib; do
    echo "extension=${ext}.so" > "%{buildroot}%{_sysconfdir}/php/conf.d/20-${ext}.ini"
done
rm -r %{buildroot}%{_libdir}/build

%files
%license LICENSE
%doc README.md NEWS
%{_bindir}/*
%{_datadir}/man/*
%dir %{_libdir}/php
%dir %{_libdir}/php/extensions
# main configuration file
%{_sysconfdir}/php/php.ini
# main configuration directory
# set in the `./configure` arguments
%dir %{_sysconfdir}/php/conf.d

%files devel
%{_includedir}/php/*

%files curl
%config(noreplace) %{_sysconfdir}/php/conf.d/20-curl.ini
%{_libdir}/php/extensions/curl.so

%files gd
%config(noreplace) %{_sysconfdir}/php/conf.d/20-gd.ini
%{_libdir}/php/extensions/gd.so

%files openssl
%config(noreplace) %{_sysconfdir}/php/conf.d/20-openssl.ini
%{_libdir}/php/extensions/openssl.so

%files pcntl
%config(noreplace) %{_sysconfdir}/php/conf.d/20-pcntl.ini
%{_libdir}/php/extensions/pcntl.so

%files zip
%config(noreplace) %{_sysconfdir}/php/conf.d/20-zip.ini
%{_libdir}/php/extensions/zip.so

%files zlib
%config(noreplace) %{_sysconfdir}/php/conf.d/20-zlib.ini
%{_libdir}/php/extensions/zlib.so

%changelog
%autochangelog
