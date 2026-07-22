# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname widgetsnbextension

Name:           python-%{srcname}
Version:        4.0.15
Release:        %autorelease
Summary:        Jupyter interactive widget extension for Notebook
License:        BSD-3-Clause
URL:            https://github.com/jupyter-widgets/ipywidgets
#!RemoteAsset:  sha256:de8610639996f1567952d763a5a41af8af37f2575a41f9852a38f947eb82a3b9
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l widgetsnbextension

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(jupyter-packaging)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Classic Jupyter Notebook extension for Jupyter interactive widgets.

%generate_buildrequires
%pyproject_buildrequires

%install -a
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_datadir}/jupyter/nbextensions/jupyter-js-widgets/
%{_sysconfdir}/jupyter/nbconfig/notebook.d/widgetsnbextension.json

%changelog
%autochangelog
