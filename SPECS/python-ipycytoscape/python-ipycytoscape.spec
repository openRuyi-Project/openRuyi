# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ipycytoscape

Name:           python-%{srcname}
Version:        1.3.3
Release:        %autorelease
Summary:        Interactive Cytoscape graphs in Jupyter
License:        BSD-3-Clause
URL:            https://github.com/cytoscape/ipycytoscape
#!RemoteAsset:  sha256:b6f3199df034f088e92d388e27e629f58ae2901b213cb9299e5b564272f9a2f8
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Use the prebuilt Jupyter assets included in the sdist.
Patch2000:      2000-use-prebuilt-jupyter-assets.patch

BuildOption(install):  -l ipycytoscape

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(ipywidgets)
BuildRequires:  python3dist(jupyter-packaging)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(spectate)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Interactive graph visualization using Cytoscape in Jupyter notebooks.

%generate_buildrequires
%pyproject_buildrequires

%install -a
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_datadir}/jupyter/labextensions/jupyter-cytoscape/
%{_datadir}/jupyter/nbextensions/jupyter-cytoscape/
%{_sysconfdir}/jupyter/nbconfig/notebook.d/jupyter-cytoscape.json

%changelog
%autochangelog
