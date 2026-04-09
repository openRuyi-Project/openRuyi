# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname markupsafe

Name:           python-markupsafe
Version:        3.0.2
Release:        %autorelease
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python
License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
#!RemoteAsset
Source0:        https://github.com/pallets/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  expat

%description
MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are
replaced so that they display as the actual characters. This mitigates
injection attacks, meaning untrusted user input can safely be displayed
on a page.

%package     -n python3-markupsafe
Summary:        %{summary}

%description -n python3-markupsafe
MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are
replaced so that they display as the actual characters. This mitigates
injection attacks, meaning untrusted user input can safely be displayed
on a page.

%prep
%autosetup -n markupsafe-%{version}
# Exclude C source from the package:
echo 'global-exclude *.c' >> MANIFEST.in
# Allow older setuptools
sed -i '/setuptools/s/>=.*"/"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files markupsafe

%files -n python3-markupsafe -f %{pyproject_files}
%doc CHANGES.rst README.md

%changelog
%autochangelog
