# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname gradio-client
%global pypi_name gradio_client

Name:           python-%{srcname}
Version:        2.5.0
Release:        %autorelease
Summary:        Python library for easily interacting with trained machine learning models
License:        Apache-2.0
URL:            https://github.com/gradio-app/gradio
#!RemoteAsset:  sha256:4cde99bad62149595c30c90876ca2e405e3a13687ecf895474f3412cb476673d
Source0:        https://files.pythonhosted.org/packages/source/g/%{srcname}/%{pypi_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
Source1:        https://raw.githubusercontent.com/gradio-app/gradio/refs/tags/@gradio/client@2.2.0/LICENSE
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -L
# Triggers ValueError due to discord.py name validation on placeholder string '<<command-name>>'.
BuildOption(check):  -e gradio_client.templates.discord_chat

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(discord-py)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Build and share delightful machine learning apps, all in Python.

%prep -a
cp %{SOURCE1} LICENSE

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
