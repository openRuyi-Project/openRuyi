# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tiktoken

Name:           python-%{srcname}
Version:        0.12.0
Release:        %autorelease
Summary:        tiktoken is a fast BPE tokeniser for use with OpenAI's models
License:        MIT AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL:            https://pypi.org/project/tiktoken/
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(pip)
BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  crate(bstr-1.0)
BuildRequires:  crate(fancy-regex-0.17)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
tiktoken is a fast BPE tokeniser for use with OpenAI's models.

%prep -a
mkdir -p ~/.cargo
cat > ~/.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSE.dependencies

%changelog
%autochangelog
