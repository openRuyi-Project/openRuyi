# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hatchling

Name:           python-%{srcname}
Version:        1.29.0
Release:        %autorelease
Summary:        The build backend used by Hatch
License:        MIT
URL:            https://pypi.org/project/hatchling
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l hatchling

BuildRequires:  python3-devel
BuildRequires:  python3-packaging
BuildRequires:  python3-pip
BuildRequires:  python3-pathspec
BuildRequires:  python3-pluggy
BuildRequires:  python3-trove-classifiers
BuildRequires:  expat

%description
This is the extensible, standards compliant build backend used by Hatch.

%package     -n python3-hatchling
Summary:        %{summary}

%description -n python3-hatchling
This is the extensible, standards compliant build backend used by Hatch.

%files -n python3-hatchling -f %{pyproject_files}
%doc README.md
%{_bindir}/hatchling

%changelog
%{?autochangelog}
