# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 904aa67e1e2d1dec92959df63e700b166d5c1022

Name:           stb
Version:        0+git20260313.904aa67
Release:        %autorelease
Summary:        stb single-file public domain libraries for C/C++
License:        MIT OR Unlicense
URL:            https://github.com/nothings/stb
#!RemoteAsset:  sha256:877d81c75a9360825e2e6d94b793d7a9affe97e2dbee97c83fc85663c25f0c27
Source:         https://github.com/nothings/stb/archive/%{commit}/stb-%{commit}.tar.gz
BuildArch:      noarch

%description
stb is a collection of single-file public domain libraries for C/C++.

%package        devel
Summary:        Development files for %{name}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n stb-%{commit}

%build
cat <<EOF > stb.pc
prefix=/usr
includedir=\${prefix}/include/stb

Name: stb
Description: Single-file image and audio processing libraries for C/C++
Version: %{version}
Cflags: -I\${includedir}
EOF

%install
mkdir -p %{buildroot}%{_includedir}/stb
cp -p *.h *.c %{buildroot}%{_includedir}/stb/
mkdir -p %{buildroot}%{_datadir}/pkgconfig
cp -p stb.pc %{buildroot}%{_datadir}/pkgconfig/

%files devel
%license LICENSE
%doc README.md docs/
%{_includedir}/stb/
%{_datadir}/pkgconfig/stb.pc

%changelog
%autochangelog
