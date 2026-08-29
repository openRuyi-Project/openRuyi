# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit0 bdc2b4550453e0ef2d3b5190f9c6103a84eff184
%global shortcommit0 bdc2b45
%global date0 20260623

Name:           warp-ctc
Version:        0+git%{date0}.%{shortcommit0}
Release:        %autorelease
Summary:        Fast parallel CTC library
License:        Apache-2.0
URL:            https://github.com/baidu-research/warp-ctc
VCS:            git:https://github.com/baidu-research/warp-ctc
#!RemoteAsset:  sha256:b027fac9f431c3378b6ec1500b401507c1eef43f16ae819090e76bc7f63bced0
Source0:        https://github.com/baidu-research/warp-ctc/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DWITH_GPU=OFF
BuildOption(conf):  -DWITH_ROCM=OFF
BuildOption(conf):  -DWITH_TORCH=OFF
BuildOption(conf):  -DCMAKE_DISABLE_FIND_PACKAGE_Torch=ON
BuildOption(conf):  -DBUILD_TESTS=OFF
BuildOption(conf):  -DBUILD_SHARED=ON
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
warp-ctc is a small library for computing the Connectionist Temporal
Classification loss and gradient.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains headers for developing applications that use %{name}.

%install -a
install -d -m 0755 %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/libwarpctc.so %{buildroot}%{_libdir}/libwarpctc.so
rmdir %{buildroot}%{_prefix}/lib
# Keep Paddle-compatible include layout for code that includes
# <warpctc/include/ctc.h>.
install -d -m 0755 %{buildroot}%{_includedir}/warpctc/include
cp -a include/* %{buildroot}%{_includedir}/warpctc/include/

%check
cat > warpctc-smoke.cc <<'EOF'
#include <ctc.h>

int main() {
  return get_warpctc_version() > 0 ? 0 : 1;
}
EOF
%{__cxx} %{build_cxxflags} -Iinclude warpctc-smoke.cc -L%{_build} \
  -Wl,-rpath,%{_build} -lwarpctc -o warpctc-smoke
./warpctc-smoke

%files
%doc README.md
%license LICENSE
%{_libdir}/libwarpctc.so

%files devel
%{_includedir}/ctc.h
%{_includedir}/warpctc/

%changelog
%autochangelog
