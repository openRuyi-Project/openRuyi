# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global rocm_version 7.2.4

Name:           rocm-core
Version:        %{rocm_version}
Release:        %autorelease
Summary:        A utility to get the ROCm release version
License:        MIT
URL:            https://github.com/ROCm/rocm-core
#!RemoteAsset:  sha256:32dab2f00e22fb5462beffae03cc642403925d22a42662e15ac0f68d8e885dea
Source0:        %{url}/archive/refs/tags/rocm-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DROCM_VERSION=%{version}

BuildRequires:  cmake

%global _description %{expand:
A utility to get the ROCm release version
}

%description
%{_description}

%package        devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{_description}

%install -a
# ROCm version is maintained by packager
# No need to use rocmmod to switch ROCm version
rm -rvf %{buildroot}/%{_exec_prefix}/.info
rm -rvf %{buildroot}/%{_libdir}/rocmmod
# Use RUNPATH instead of RPATH on Linux distribution
rm -vf %{buildroot}/%{_exec_prefix}/libexec/rocm-core/runpath_to_rpath.py
rm -rvf %{buildroot}/%{_exec_prefix}/share/doc/*/LICENSE.md

%files
%doc README.md
%license LICENSE.md
%{_bindir}/rdhc
%{_libdir}/librocm-core.so.*
%{_libexecdir}/rocm-core/
%{_datadir}/rdhc/

%files devel
%{_includedir}/rocm-core/*.h
%{_libdir}/cmake/rocm-core/*.cmake
%{_libdir}/librocm-core.so

%changelog
%autochangelog
