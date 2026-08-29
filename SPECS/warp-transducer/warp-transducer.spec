# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit0 7ea6bfe748779c245a0fcaa5dd9383826273eff2
%global shortcommit0 7ea6bfe
%global date0 20260623

Name:           warp-transducer
Version:        0+git%{date0}.%{shortcommit0}
Release:        %autorelease
Summary:        Fast parallel RNN transducer loss library
License:        Apache-2.0
URL:            https://github.com/PaddlePaddle/warp-transducer
VCS:            git:https://github.com/PaddlePaddle/warp-transducer
#!RemoteAsset:  sha256:2c176e823d0f7049b274169a0c1f705cd85ce1d128b0f9f2f8946afdb15bb46b
Source0:        https://github.com/PaddlePaddle/warp-transducer/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DWITH_GPU=OFF
BuildOption(conf):  -DWITH_ROCM=OFF
BuildOption(conf):  -DBUILD_TESTS=OFF
BuildOption(conf):  -DBUILD_SHARED=ON
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
warp-transducer is a small library for computing the RNN transducer loss and
gradient.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains headers for developing applications that use %{name}.

%install -a
install -d -m 0755 %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/libwarprnnt.so %{buildroot}%{_libdir}/libwarprnnt.so
rmdir %{buildroot}%{_prefix}/lib
# Keep Paddle-compatible include layout for code that includes
# <warprnnt/include/rnnt.h>.
install -d -m 0755 %{buildroot}%{_includedir}/warprnnt/include
cp -a include/* %{buildroot}%{_includedir}/warprnnt/include/

%check
cat > warprnnt-smoke.cc <<'EOF'
#include <rnnt.h>

int main() {
  return get_warprnnt_version() > 0 ? 0 : 1;
}
EOF
%{__cxx} %{build_cxxflags} -Iinclude warprnnt-smoke.cc -L%{_build} \
  -Wl,-rpath,%{_build} -lwarprnnt -o warprnnt-smoke
./warprnnt-smoke

%files
%doc README.md
%license LICENSE
%{_libdir}/libwarprnnt.so

%files devel
%{_includedir}/rnnt.h
%{_includedir}/warprnnt/

%changelog
%autochangelog
