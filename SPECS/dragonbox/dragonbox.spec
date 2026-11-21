# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dragonbox
Version:        1.1.3
Release:        %autorelease
Summary:        Floating-point to decimal conversion for C++
License:        BSL-1.0 OR (Apache-2.0 WITH LLVM-exception)
URL:            https://github.com/jk-jeon/dragonbox
#!RemoteAsset:  sha256:09d63b05e9c594ec423778ab59b7a5aa1d76fdd71d25c7048b0258c4ec9c3384
Source0:        https://github.com/jk-jeon/dragonbox/archive/refs/tags/%{version}.tar.gz#/dragonbox-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DDRAGONBOX_INSTALL_TO_CHARS=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Dragonbox computes the shortest decimal representation that rounds back
to a binary floating-point value.

%package        devel
Summary:        C++ conversion headers and CMake targets for Dragonbox

%description    devel
Headers and imported CMake targets for using the Dragonbox algorithm.

%install -a
ln -s %{name}-%{version}/%{name} %{buildroot}%{_includedir}/%{name}

%check
# Build and run the floating-point conversion tests with FetchContent restricted to local inputs.
%cmake -S subproject/test -B build-tests -DFETCHCONTENT_FULLY_DISCONNECTED=ON
cmake --build build-tests --parallel %{_smp_build_ncpus}
ctest --test-dir build-tests --output-on-failure

%files devel
%doc README.md
%license LICENSE-Apache2-LLVM LICENSE-Boost
%{_includedir}/dragonbox
%{_includedir}/dragonbox-%{version}/
%{_libdir}/cmake/dragonbox-%{version}/

%changelog
%autochangelog
