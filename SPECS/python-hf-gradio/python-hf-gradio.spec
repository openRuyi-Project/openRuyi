# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hf-gradio
%global pypi_name hf_gradio

Name:           python-%{srcname}
Version:        0.4.1
Release:        %autorelease
Summary:        An extension of the Hugging Face CLI for interacting with Gradio Spaces and Apps
License:        MIT
URL:            https://github.com/gradio-app/hf-gradio
#!RemoteAsset:  sha256:a017d942618f0d495a58ee4563047fa04bef614c00e0cb789a9a6d0633cffa7b
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
An extension of the Hugging Face CLI for interacting with Gradio Spaces and Apps.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/hf-gradio

%changelog
%autochangelog
