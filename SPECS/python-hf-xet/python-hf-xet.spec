# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hf_xet

Name:           python-hf-xet
Version:        1.3.2
Release:        %autorelease
Summary:        Fast transfer layer for large files on Hugging Face Hub
License:        Apache-2.0
URL:            https://pypi.org/project/hf-xet/
VCS:            git:https://github.com/huggingface/xet-core
#!RemoteAsset:  sha256:e130ee08984783d12717444e538587fa2119385e5bd8fc2bb9f930419b73a7af
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
# TODO(vendor): if OBS cannot access GitHub release directly, switch to _service(download_url) as fallback.
#!RemoteAsset:  sha256:3700b275ebb7f821fcf8ff7b3943670c3d5820f98a292881ae9e1f5d8fb8a252
Source1:        https://github.com/software-vendor/python-hf-xet/releases/download/vendor-%{version}/hf_xet-%{version}-vendor.tar.zst
BuildSystem:    pyproject

BuildOption(prep):  -a1
BuildOption(install):  hf_xet

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(maturin)
BuildRequires:  rust
BuildRequires:  cargo

Provides:       python3-hf-xet = %{version}-%{release}
Provides:       python3-hf-xet%{?_isa} = %{version}-%{release}
%python_provide python3-hf-xet

%description
Hf-xet provides fast transfer support for large model and dataset files in the
Hugging Face Hub ecosystem.

%prep -a
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF2'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF2

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license hf_xet/LICENSE

%changelog
%autochangelog
