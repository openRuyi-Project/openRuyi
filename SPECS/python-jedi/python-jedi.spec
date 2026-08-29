# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jedi

Name:           python-%{srcname}
Version:        0.20.0
Release:        %autorelease
Summary:        Autocompletion tool for Python that can be used for text editors
License:        MIT
URL:            https://github.com/davidhalter/jedi
#!RemoteAsset:  sha256:c3f4ccbd276696f4b19c54618d4fb18f9fc24b0aef02acf704b23f487daa1011
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Jedi is a static analysis tool for Python that is typically used
in IDEs/editors plugins. Jedi has a focus on autocompletion and
goto functionality. Other features include refactoring, code
search and finding references.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
