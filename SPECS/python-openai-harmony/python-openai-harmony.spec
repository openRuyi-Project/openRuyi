# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           python-openai-harmony
Version:        0.0.8
Release:        %autorelease
Summary:        OpenAI's response format for its open-weight model series gpt-oss
License:        Apache-2.0
URL:            https://github.com/openai/harmony
VCS:            git:https://github.com/openai/harmony.git
#!RemoteAsset:  sha256:6e43f98e6c242fa2de6f8ea12eab24af63fa2ed3e89c06341fb9d92632c5cbdf
Source0:        https://files.pythonhosted.org/packages/source/o/openai-harmony/openai_harmony-%{version}.tar.gz

BuildRequires:  pkgconfig(python3)
# 核心依赖：解析 pyproject.toml 并调用 Rust 编译所需的工具
BuildRequires:  python3-maturin
BuildRequires:  rust
BuildRequires:  cargo

%description
OpenAI Harmony is the response format for its open-weight model series gpt-oss.
The format enables the model to output to multiple different channels for chain of thought,
and tool calling preambles along with regular responses. The majority of the rendering
and parsing is built in Rust for performance and exposed to Python through pyo3 bindings.

%prep
# Python 源码包解压后通常会将短横线转换为下划线，请根据实际解压目录名确认
%autosetup -n openai_harmony-%{version}

%build
# 自动调用 maturin 和 cargo 进行跨语言编译，并生成 wheel 包
%pyproject_wheel

%install
# 将生成的 wheel 包安装到 buildroot 目录
%pyproject_install

%files
# 注意：核实源码包解压后是否真的有 LICENSE 和 README.md，没有则需调整
%license LICENSE
%doc README.md
# 极其关键：因为包含了 Rust 编译出的动态链接库（.so），它属于架构相关包
# 必须使用 %{python3_sitearch} 而不能用 %{python3_sitelib}
%{python3_sitearch}/openai_harmony/
%{python3_sitearch}/openai_harmony-%{version}.dist-info/

%changelog
%autochangelog
