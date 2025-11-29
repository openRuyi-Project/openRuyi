# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wyhash
Version:        4
Release:        %autorelease
Summary:        Fast portable non-cryptographic hash function
License:        Unlicense
URL:            https://github.com/wangyi-fudan/wyhash
#!RemoteAsset
Source:         https://github.com/wangyi-fudan/wyhash/archive/refs/tags/wyhash_final%{version}.tar.gz

%description
wyhash is a fast, portable, non-cryptographic hash function and pseudorandom
number generator.

%package        devel
Summary:        Development files for %{name}

%description    devel
This package contains the header files for using wyhash.

%prep
%autosetup -p1 -n wyhash-wyhash_final%{version}

%install
install -d -m 0755 %{buildroot}%{_includedir}
install -p -m 0644 wyhash.h %{buildroot}%{_includedir}/
install -p -m 0644 wyhash32.h %{buildroot}%{_includedir}/

%files devel
%license LICENSE
%doc README.md
%{_includedir}/wyhash.h
%{_includedir}/wyhash32.h

%changelog
%{?autochangelog}
