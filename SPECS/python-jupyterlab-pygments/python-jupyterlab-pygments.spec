# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jupyterlab-pygments
%global pypi_name jupyterlab_pygments

Name:           python-%{srcname}
Version:        0.3.0
Release:        %autorelease
Summary:        Pygments theme using JupyterLab CSS variables
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyterlab_pygments
#!RemoteAsset:  sha256:721aca4d9029252b11cfa9d185e5b5af4d54772bb8072f9b7036f4170054d35d
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Use the prebuilt labextension to break the JupyterLab dependency cycle.
Patch2000:      2000-drop-jupyterlab-build-requirement.patch

BuildOption(install):  -l jupyterlab_pygments

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatch-jupyter-builder)
BuildRequires:  python3dist(hatch-nodejs-version)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pygments)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
jupyterlab-pygments provides a Pygments theme based on JupyterLab CSS
variables for consistent notebook syntax highlighting.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_datadir}/jupyter/labextensions/%{pypi_name}

%changelog
%autochangelog
