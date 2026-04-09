# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           vmaf
Version:        3.0.0
Release:        %autorelease
Summary:        Video Multi-Method Assessment Fusion
License:        BSD-2-Clause-Patent
URL:            https://github.com/netflix/vmaf
#!RemoteAsset
Source:         https://github.com/Netflix/vmaf/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Ddefault_library=shared
BuildOption(conf):  -Dbuilt_in_models=true

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  nasm
BuildRequires:  xxd

%description
VMAF is a perceptual video quality assessment algorithm developed by Netflix.
This package contains the command-line tools.

%package        devel
Summary:        Development files for VMAF
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing applications
that use VMAF.

%conf -p
cd libvmaf

%build -p
cd libvmaf

%install -p
cd libvmaf

%install -a
cd ..
mkdir -p %{buildroot}%{_datadir}/%{name}/model/
cp -Rp model/* %{buildroot}%{_datadir}/%{name}/model/

%check
cd libvmaf
%meson_test

%files
%doc README.md CHANGELOG.md
%{_bindir}/vmaf
%{_datadir}/vmaf/model/
%license LICENSE
%{_libdir}/libvmaf.so.*

%files devel
%doc CONTRIBUTING.md
%{_includedir}/libvmaf/
%{_libdir}/libvmaf.so
%{_libdir}/pkgconfig/libvmaf.pc

%changelog
%autochangelog
