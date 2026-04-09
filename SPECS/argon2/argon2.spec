# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           argon2
Version:        20190702
Release:        %autorelease
Summary:        The password-hashing tools
License:        CC0-1.0 OR Apache-2.0
URL:            https://github.com/P-H-C/phc-winner-argon2
#!RemoteAsset
Source:         https://github.com/P-H-C/phc-winner-argon2/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  -j1
BuildOption(build):  CFLAGS="%{optflags} -Iinclude"
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  LIBRARY_REL=%{_lib}

BuildRequires:  gcc
BuildRequires:  make

%description
Argon2 is a password-hashing function that can be used to hash passwords
for credential storage, key derivation, or other applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep -a
# Honours default RPM build options and library path, do not use -march=native
sed -e '/^CFLAGS/s:^CFLAGS:LDFLAGS=%{build_ldflags}\nCFLAGS:' \
    -e 's:-O3 -Wall:%{optflags}:' \
    -e '/^LIBRARY_REL/s:lib:%{_lib}:' \
    -e 's:-march=\$(OPTTARGET) :${CFLAGS} :' \
    -e 's:CFLAGS += -march=\$(OPTTARGET)::' \
    -i Makefile

# Fix pkgconfig file
sed -e 's:lib/@HOST_MULTIARCH@:%{_lib}:;s/@UPSTREAM_VER@/%{version}/' -i libargon2.pc.in

# No configure
%conf

%install -a
rm %{buildroot}%{_libdir}/libargon2.a
install -Dpm 644 libargon2.pc %{buildroot}%{_libdir}/pkgconfig/libargon2.pc
chmod -x %{buildroot}%{_includedir}/%{name}.h

%files
%license LICENSE
%{_bindir}/argon2
%{_libdir}/libargon2.so.*

%files devel
%doc *md
%{_includedir}/%{name}.h
%{_libdir}/libargon2.so
%{_libdir}/pkgconfig/libargon2.pc

%changelog
%autochangelog
