# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global build_number 1812-0
# Run the upstream common-library and database-engine unit suites.
%global _test_target run_tests

# Firebird loads these plugins from private directories.
%global __provides_exclude_from ^%{_libdir}/firebird/.*$

Name:           firebird
Version:        5.0.4
Release:        %autorelease
Summary:        Firebird embedded SQL database engine and client tools
License:        Interbase-1.0 AND LicenseRef-openRuyi-IDPL-1.0 AND BSD-3-Clause AND BSD-4-Clause AND LicenseRef-openRuyi-Public-Domain
URL:            https://firebirdsql.org/
VCS:            git:https://github.com/FirebirdSQL/firebird.git
#!RemoteAsset:  sha256:5041b97b480c9fe241c92ad0adf89e36faad0a8f0e21f1371dfbcc96a6f38e12
Source0:        https://github.com/FirebirdSQL/firebird/releases/download/v%{version}/Firebird-%{version}.%{build_number}-source.tar.xz
Source1:        THIRD-PARTY-NOTICES.txt
BuildSystem:    autotools

# LibreOffice's merged backup difference-file access restriction.
Patch1000:      1000-check-backup-difference-file-access.patch
# Use packaged generators, numeric libraries and integer headers.
Patch2000:      2000-use-installed-generators-and-numeric-libraries.patch

BuildOption(prep):  -n Firebird-%{version}.%{build_number}-source
BuildOption(conf):  --with-system-editline
BuildOption(conf):  --with-system-boost
BuildOption(conf):  --with-system-re2
# Match Firebird and RE2 when Autoconf probes system C++ headers.
BuildOption(conf):  CXXFLAGS="%{build_cxxflags} -std=c++17"
BuildOption(conf):  --with-fbtzdata=%{_datadir}/firebird/tzdata
BuildOption(conf):  --with-fbbin=%{_bindir}
BuildOption(conf):  --with-fbsbin=%{_sbindir}
BuildOption(conf):  --with-fbconf=%{_sysconfdir}/firebird
BuildOption(conf):  --with-fblib=%{_libdir}
BuildOption(conf):  --with-fbinclude=%{_includedir}
BuildOption(conf):  --with-fbintl=%{_libdir}/firebird/intl
BuildOption(conf):  --with-fbsecure-db=%{_sharedstatedir}/firebird
BuildOption(conf):  --with-fbmsg=%{_datadir}/firebird
BuildOption(conf):  --with-fblog=%{_localstatedir}/log/firebird
BuildOption(conf):  --with-fbplugins=%{_libdir}/firebird/plugins
BuildOption(build):  CFLAGS="%{build_cflags}"
BuildOption(build):  CXXFLAGS="%{build_cxxflags} -fno-lifetime-dse -fno-strict-aliasing"
BuildOption(build):  LDFLAGS="%{build_ldflags}"

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  cloop
BuildRequires:  firebird-btyacc
BuildRequires:  firebird-ttmath-devel
BuildRequires:  gcc-c++
BuildRequires:  libcds-devel(firebird-michael-kv-update)
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  unzip
BuildRequires:  pkgconfig(decnumber)
BuildRequires:  pkgconfig(libcds)
BuildRequires:  pkgconfig(libtomcrypt)
BuildRequires:  pkgconfig(re2)
%ifarch riscv64
BuildRequires:  pkgconfig(atomic_ops)
%endif
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libtommath)
BuildRequires:  pkgconfig(tinfo)
BuildRequires:  pkgconfig(zlib)

Requires:       icu4c

%description
Firebird supplies an in-process SQL engine for ODS 13.1 databases. Its
command-line tools execute SQL and back up or restore local databases.

%package        devel
Summary:        Headers and client development files for Firebird
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel

%description    devel
Firebird client headers, linker files and fb_config for building
applications that use the embedded SQL engine.

%prep -a
cp -p %{SOURCE1} THIRD-PARTY-NOTICES.txt

%conf -p
autoreconf -fiv

%install
(cd gen && sh install/makeInstallImage.sh)
image=gen/buildroot
install -d %{buildroot}{%{_bindir},%{_includedir}/firebird,%{_libdir},%{_datadir}/firebird,%{_sysconfdir}/firebird}
cp -a "$image"%{_libdir}/libfbclient.so* %{buildroot}%{_libdir}/
cp -a "$image"%{_libdir}/firebird %{buildroot}%{_libdir}/
install -pm 0755 "$image"%{_libdir}/libib_util.so %{buildroot}%{_libdir}/
tar -C "$image"%{_includedir}/firebird --exclude='./impl/boost' -cf - . | tar -C %{buildroot}%{_includedir}/firebird -xf -
install -pm 0644 "$image"%{_includedir}/{ibase.h,iberror.h,ib_util.h} %{buildroot}%{_includedir}/
install -pm 0755 "$image"%{_bindir}/isql %{buildroot}%{_bindir}/firebird-isql
install -pm 0755 "$image"%{_bindir}/gbak "$image"%{_sbindir}/fb_config %{buildroot}%{_bindir}/
install -pm 0644 "$image"%{_sysconfdir}/firebird/{databases.conf,firebird.conf,plugins.conf} %{buildroot}%{_sysconfdir}/firebird/
install -pm 0644 "$image"%{_datadir}/firebird/firebird.msg %{buildroot}%{_datadir}/firebird/

%files
%doc README.md
%license builds/install/misc/IDPLicense.txt builds/install/misc/IPLicense.txt THIRD-PARTY-NOTICES.txt
%dir %{_sysconfdir}/firebird
%config(noreplace) %{_sysconfdir}/firebird/*.conf
%{_bindir}/firebird-isql
%{_bindir}/gbak
%{_datadir}/firebird/
%{_libdir}/firebird/
%{_libdir}/libfbclient.so.*
%{_libdir}/libib_util.so

%files devel
%{_bindir}/fb_config
%{_includedir}/firebird/
%{_includedir}/ib_util.h
%{_includedir}/ibase.h
%{_includedir}/iberror.h
%{_libdir}/libfbclient.so

%changelog
%autochangelog
