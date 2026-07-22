# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jupyterlab-widgets
%global pypi_name jupyterlab_widgets

Name:           python-%{srcname}
Version:        3.0.16
Release:        %autorelease
Summary:        Jupyter interactive widgets for JupyterLab
License:        BSD-3-Clause
URL:            https://github.com/jupyter-widgets/ipywidgets
#!RemoteAsset:  sha256:423da05071d55cf27a9e602216d35a3a65a3e41cdf9c5d3b643b814ce38c19e0
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Use the prebuilt JupyterLab extension included in the sdist.
Patch2000:      2000-drop-jupyterlab-build-requirement.patch

BuildOption(install):  -l jupyterlab_widgets

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatch-jupyter-builder)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Prebuilt JupyterLab extension for Jupyter interactive widgets.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_datadir}/jupyter/labextensions/@jupyter-widgets/jupyterlab-manager/

%changelog
%autochangelog
