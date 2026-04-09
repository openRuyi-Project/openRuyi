# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global pypi_name cppheaderparser
%global pkg_name CppHeaderParser

Name:           python-%{pypi_name}
Version:        2.7.4
Release:        %autorelease
Summary:        Parse C++ header files and generate a data structure
License:        BSD-3-Clause
URL:            http://senexcanis.com/open-source/cppheaderparser/
#!RemoteAsset
Source0:        https://pypi.org/packages/source/c/CppHeaderParser/CppHeaderParser-%{version}.tar.gz
# https://github.com/robotpy/robotpy-cppheaderparser/blob/main/LICENSE.txt
# The author does not provide a license file in 2.7.4 source code
Source1:        LICENSE.txt
BuildArch:      noarch
BuildSystem:    pyproject

Patch0:         0001-cppheaderparser-silence-invalid-escape-sequence.patch

BuildOption(install):  -l %{pkg_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip) >= 19
BuildRequires:  python3dist(ply)

%description
Parse C++ header files and generate a data structure representing the
class.

%prep -a
cp %{SOURCE1} .
rm -rf %{pypi_name}.egg-info
# Remove outdated parts (Python 2.x)
rm -rf CppHeaderParser/{examples,docs}
sed -i -e '/^#!\//, 1d' CppHeaderParser/CppHeaderParser.py

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.txt README.html

%changelog
%autochangelog
