# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           unicode-ucd
Version:        17.0.0
Release:        %autorelease
Summary:        Unicode Character Database
License:        Unicode-3.0
URL:            https://www.unicode.org/ucd/
# VCS: No VCS link available
#!RemoteAsset
Source0:        https://www.unicode.org/Public/%{version}/ucd/UCD.zip
#!RemoteAsset
Source1:        https://www.unicode.org/Public/%{version}/ucd/Unihan.zip
#!RemoteAsset
Source2:        https://www.unicode.org/license.txt
BuildArch:      noarch

BuildRequires:  unzip

%description
The Unicode Character Database (UCD) consists of a number of data files listing
Unicode character properties and related data. It also includes data files
containing test data for conformance to several important Unicode algorithms.

%prep
%autosetup -c

%conf
# No configure

%build
# No build

%install
mkdir -p %{buildroot}%{_datadir}/unicode/ucd
cp -ar . %{buildroot}%{_datadir}/unicode/ucd
cp %{SOURCE2} .

%files
%license license.txt
%dir %{_datadir}/unicode/
%{_datadir}/unicode/ucd

%changelog
%autochangelog
