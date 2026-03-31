# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname langcodes

Name:           python-%{srcname}
Version:        3.5.1
Release:        %autorelease
Summary:        Tools for labeling human languages with IETF language tags
License:        MIT
URL:            https://github.com/georgkrause/langcodes
#!RemoteAsset:  sha256:40bff315e01b01d11c2ae3928dd4f5cbd74dd38f9bd912c12b9a3606c143f731
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Langcodes knows what languages are. It knows the standardized codes
that refer to them, such as en for English, es for Spanish and hi for Hindi.
These are IETF language tags. You may know them by their old name,
ISO 639 language codes. IETF has done some important things for
backward compatibility and supporting language variations that you
won't find in the ISO standard.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%{?autochangelog}
