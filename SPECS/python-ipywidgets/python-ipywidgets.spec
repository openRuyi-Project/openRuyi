# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ipywidgets

Name:           python-%{srcname}
Version:        8.1.8
Release:        %autorelease
Summary:        Jupyter interactive widgets
License:        BSD-3-Clause
URL:            https://github.com/jupyter-widgets/ipywidgets
#!RemoteAsset:  sha256:61f969306b95f85fba6b6986b7fe45d73124d1d9e3023a8068710d47a22ea668
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l ipywidgets

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(comm)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(jupyterlab-widgets)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(traitlets)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(widgetsnbextension)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
