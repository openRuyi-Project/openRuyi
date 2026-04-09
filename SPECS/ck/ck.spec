# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ck
Version:        0.7.2
Release:        %autorelease
Summary:        Library for high performance concurrent programming
License:        BSD-2-Clause AND Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/concurrencykit/ck
#!RemoteAsset:  sha256:568ebe0bc1988a23843fce6426602e555b7840bf6714edcdf0ed530214977f1b
Source0:        https://github.com/concurrencykit/ck/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description
Concurrency Kit provides a plethora of concurrency primitives, safe memory
reclamation mechanisms and lock-less and lock-free data structures.

%package        devel
Summary:        Header files and libraries for CK development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for Concurrency Kit.

# Not standrad configure.
%conf
export CFLAGS="%{optflags}"
./configure \
    --libdir=%{_libdir} \
    --includedir=%{_includedir}/%{name} \
    --mandir=%{_mandir} \
    --prefix=%{_prefix}

%install -a
rm -f %{buildroot}%{_libdir}/libck.a

%check
# TODO: skip tests for now.

%files
%license LICENSE
%{_libdir}/libck.so.*

%files devel
%{_libdir}/libck.so
%{_includedir}/ck/
%{_libdir}/pkgconfig/ck.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
