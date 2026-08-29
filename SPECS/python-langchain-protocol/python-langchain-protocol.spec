# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname langchain-protocol
%global pypi_name langchain_protocol

Name:           python-%{srcname}
Version:        0.0.16
Release:        %autorelease
Summary:        Python bindings for the LangChain agent streaming protocol
License:        MIT
URL:            https://github.com/langchain-ai/agent-protocol
VCS:            git:https://github.com/langchain-ai/agent-protocol.git
#!RemoteAsset:  sha256:806c7cdd951b1c4f692fa40fce60821ff0f221d4360e27673ddf2c2b99c2b7ff
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
langchain-protocol provides generated Python typing primitives for the
LangChain agent streaming protocol.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
