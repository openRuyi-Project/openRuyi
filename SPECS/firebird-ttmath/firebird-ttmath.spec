# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           firebird-ttmath
Version:        0.9.3
Release:        %autorelease
Summary:        TTMath integer headers adapted for Firebird
License:        BSD-3-Clause
URL:            https://www.ttmath.org/
VCS:            git:https://gitea.ttmath.org/tomasz.sowa/ttmath.git
#!RemoteAsset:  sha256:4a9a7d1d377fc3907fb75facd4817ba6ac9d60bb4837584256467a54705c6fde
Source0:        https://downloads.sourceforge.net/project/ttmath/ttmath/ttmath-%{version}/ttmath-%{version}-src.tar.gz
Source1:        integer-check.cpp
Patch1000:      1000-adapt-integer-storage-for-firebird.patch
Patch1001:      1001-preserve-sign-in-right-shifts.patch

BuildArch:      noarch
BuildRequires:  gcc-c++

%description
The TTMath integer backend used by Firebird retains eight-byte-compatible
storage and trivial constructors for database descriptors and unions.

%package        devel
Summary:        Integer headers for the Firebird TTMath backend

%description    devel
Firebird's integer-only TTMath headers, including its storage adaptations
and signed shift fix. These headers use a private include directory.

%prep
%autosetup -p1 -n ttmath-%{version}

%install
install -d %{buildroot}%{_includedir}/firebird-ttmath
for header in ttmath.h ttmathint.h ttmathuint.h ttmathtypes.h ttmathmisc.h ttmathobjects.h ttmaththreads.h ttmathuint_x86.h ttmathuint_x86_64.h ttmathuint_noasm.h; do
    install -pm 0644 ttmath/$header %{buildroot}%{_includedir}/firebird-ttmath/
done

%check
# Check the installed integer headers with Firebird's storage and shift requirements.
%{__cxx} %{build_cxxflags} -std=c++17 -I%{buildroot}%{_includedir} %{SOURCE1} %{build_ldflags} -o integer-check
./integer-check

%files devel
%license COPYRIGHT
%{_includedir}/firebird-ttmath/

%changelog
%autochangelog
