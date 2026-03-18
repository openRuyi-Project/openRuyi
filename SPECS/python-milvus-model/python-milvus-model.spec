# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname milvus-model

Name:           python-%{srcname}
Version:        0.3.2
Release:        %autorelease
Summary:        Model components for PyMilvus, the Python SDK for Milvus
License:        Apache-2.0
URL:            https://github.com/milvus-io/milvus-model
# v0.3.2 is not published on PyPI, use GitHub tarball instead
#!RemoteAsset
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Upstream uses setuptools_scm for versioning which requires a git repo.
# Since we build from a tarball, patch pyproject.toml in %%prep to use a
# static version string instead.
BuildOption(install):  pymilvus

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
# build-system.requires (gitpython and setuptools_scm removed in %%prep)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
# core runtime dependencies from pyproject.toml [dependencies]
BuildRequires:  python3dist(transformers)
BuildRequires:  python3dist(onnxruntime)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(protobuf)
BuildRequires:  python3dist(numpy)
# optional dependencies for a fully functional milvus-model package
BuildRequires:  python3dist(cohere)
BuildRequires:  python3dist(datasets)
BuildRequires:  python3dist(flagembedding)
BuildRequires:  python3dist(mistralai)
BuildRequires:  python3dist(nltk)
BuildRequires:  python3dist(nomic)
BuildRequires:  python3dist(openai)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(sentence-transformers)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(voyageai)
BuildRequires:  python3dist(peft)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The milvus-model library provides model components for PyMilvus, the official
Python SDK for Milvus, an open-source vector database built for AI applications.

%prep -a
# Replace setuptools_scm dynamic versioning with a static version string
# so the package can be built from a tarball without a git repository.
sed -i \
  -e 's/dynamic = \["version"\]/version = "%{version}"/' \
  -e '/^requires.*=/,/^\]/{ /gitpython/d; /setuptools_scm/d; }' \
  -e '/\[tool\.setuptools\.dynamic\]/,/^$/{d}' \
  -e '/\[tool\.setuptools_scm\]/,/^$/{d}' \
  pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%{?autochangelog}
