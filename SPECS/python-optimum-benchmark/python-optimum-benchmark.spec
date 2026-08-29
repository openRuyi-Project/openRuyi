# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname optimum-benchmark
%global pypi_name optimum_benchmark

Name:           python-%{srcname}
Version:        0.6.0
Release:        %autorelease
Summary:        unified multi-backend utility for benchmarking Transformers, Timm, PEFT, Diffusers and Sentence-Transformers
License:        Apache-2.0
URL:            https://github.com/huggingface/optimum-benchmark
#!RemoteAsset:  sha256:8fc8c0ee4efa0e39f40a68fbee7fa9d4324a156821c65922d7b1bed8d12cc36a
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

Patch2000:      2000-fix-backends-handle-SpecialTokensMixin-import-for-tr.patch

BuildOption(install):  -l %{pypi_name}
# No module named 'llama_cpp'
BuildOption(check):  -e optimum_benchmark.backends.llama_cpp.backend
# No module named 'py_txi'
BuildOption(check):  -e optimum_benchmark.backends.py_txi.backend
# No module named 'vllm'
BuildOption(check):  -e optimum_benchmark.backends.vllm.backend
# No module named 'optimum-onnx'
BuildOption(check):  -e optimum_benchmark.profilers.ort_profiler
BuildOption(check):  -e optimum_benchmark.backends.onnxruntime.backend
# Skip ONNX tests to prevent Protobuf core dump caused by onnx/onnxruntime conflict.
BuildOption(check):  -e optimum_benchmark.backends.onnxruntime.utils

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(onnxruntime)
BuildRequires:  python3dist(pillow)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Optimum-Benchmark is a unified multi-backend utility
for benchmarking Transformers, Timm, Diffusers and
Sentence-Transformers with full support of Optimum's
hardware optimizations & quantization schemes.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/optimum-benchmark

%changelog
%autochangelog
