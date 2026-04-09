# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zephyr Du <zhonghang.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# From: https://gitlab.archlinux.org/archlinux/packaging/packages/php/-/blob/main/PKGBUILD
#     > LTO is incompatible with global registers and results in reduced performance:
#     > https://gitlab.archlinux.org/archlinux/packaging/packages/php/-/merge_requests/3
%global _lto_cflags %{nil}

%global _test_target test

Name:           php
Version:        8.5.2
Release:        %autorelease
Summary:        The PHP Interpreter
License:        PHP-3.01
URL:            https://www.php.net
VCS:            git:https://github.com/php/php-src
#!RemoteAsset
Source0:        https://www.php.net/distributions/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --enable-re2c-cgoto
BuildOption(conf):  --with-config-file-path=%{_sysconfdir}/php
BuildOption(conf):  --with-config-file-scan-dir=%{_sysconfdir}/php.d
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

BuildRequires:  re2c
BuildRequires:  bison
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libxml-2.0)

%description
PHP is a popular general-purpose scripting language that is especially suited
to web development. Fast, flexible and pragmatic, PHP powers everything from
your blog to the most popular websites in the world.

%package        devel
Summary:        Files for developing with php
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Includes and definitions for developing with php.

%install -a
install -D -m644 "php.ini-production" "%{buildroot}/etc/php/php.ini"
install -d -m755 "%{buildroot}/etc/php/conf.d/"
rm -r %{buildroot}%{_libdir}/build

%files
%license LICENSE
%doc README.md NEWS
%{_bindir}/*
%{_datadir}/man/*
# main configuration file
%{_sysconfdir}/php/php.ini
# main configuration directory
# set in the `./configure` arguments
%dir %{_sysconfdir}/php/conf.d

%files devel
%{_includedir}/php/*

%changelog
%autochangelog
