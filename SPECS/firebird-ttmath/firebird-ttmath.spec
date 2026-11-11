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
BuildArch:      noarch

# Backport only the TTMath integer storage and constructor changes.
# https://github.com/FirebirdSQL/firebird/commit/861d536fc26542335f0fb84cdea825e891364057
Patch1000:      1000-adapt-integer-storage-for-firebird.patch
# Backport signed right-shift extension for the adapted INT128 backend.
# https://github.com/FirebirdSQL/firebird/commit/3da900bf178eb45500dd774e6d22c99683e47d25
Patch1001:      1001-preserve-sign-in-right-shifts.patch

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
install -Dpm 0644 -t %{buildroot}%{_includedir}/firebird-ttmath \
    ttmath/ttmath.h ttmath/ttmathint.h ttmath/ttmathuint.h \
    ttmath/ttmathtypes.h ttmath/ttmathmisc.h ttmath/ttmathobjects.h \
    ttmath/ttmaththreads.h \
    ttmath/ttmathuint_x86.h ttmath/ttmathuint_x86_64.h ttmath/ttmathuint_noasm.h

%files devel
%license COPYRIGHT
%{_includedir}/firebird-ttmath/

%changelog
%autochangelog
