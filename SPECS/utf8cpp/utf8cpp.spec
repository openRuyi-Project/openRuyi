# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           utf8cpp
Version:        4.0.8
Release:        %autorelease
Summary:        A simple, portable and lightweight library for handling UTF-8 encoded strings
License:        BSL-1.0
URL:            https://github.com/nemtrif/utfcpp
#!RemoteAsset
Source0:        https://github.com/nemtrif/utfcpp/archive/v%{version}/utfcpp-%{version}.tar.gz
BuildSystem:    cmake

# put cmake import file in correct directory
Patch0:         utf8cpp-cmake.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
%{summary}.

Features include:
 - iterating through UTF-8 encoded strings
 - converting between UTF-8 and UTF-16/UTF-32
 - detecting invalid UTF-8 sequences

%install -a
pushd %{buildroot}%{_includedir}
ln -s utf8cpp/utf8.h ./
mkdir utf8
for f in {{un,}checked,core,cpp{11,17,20}}.h ; do
    ln -s ../utf8cpp/utf8/${f} utf8/
done
popd

%files
%doc README.md
%license LICENSE
%{_includedir}/utf8.h
%dir %{_includedir}/utf8
%{_includedir}/utf8/checked.h
%{_includedir}/utf8/core.h
%{_includedir}/utf8/cpp11.h
%{_includedir}/utf8/cpp17.h
%{_includedir}/utf8/cpp20.h
%{_includedir}/utf8/unchecked.h
%{_includedir}/utf8cpp
%{_datadir}/cmake/utf8cpp

%changelog
%autochangelog
