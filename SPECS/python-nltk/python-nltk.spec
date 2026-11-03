# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nltk

Name:           python-%{srcname}
Version:        3.10.4
Release:        %autorelease
Summary:        Natural Language Toolkit
License:        Apache-2.0
URL:            https://www.nltk.org/
#!RemoteAsset:  sha256:44679f4e9220abfd496d2c8cdb22f8425ccbe557604f9aa5cacb1c44003dabc1
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Exclude modules that require external NLTK corpora or optional integrations
# during import. Keep the rest of the runtime surface under import checking.
BuildOption(install):  -l %{srcname}
BuildOption(check):  -e nltk.book
BuildOption(check):  -e nltk.langnames
BuildOption(check):  -e nltk.tokenize.nist
BuildOption(check):  -e "nltk.test*"
BuildOption(check):  -e "nltk.app*"
BuildOption(check):  -e "nltk.draw*"
BuildOption(check):  -e "nltk.twitter*"
BuildOption(check):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(regex) >= 2021.8.3
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
NLTK provides a broad collection of libraries and tools for natural language
processing.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -q \
    nltk/test/unit/test_maxent_save_security.py \
    nltk/test/unit/test_pathsec_sweep_chunk.py \
    nltk/test/unit/test_pickle_allowlist_security.py::test_allowlist_blocks_unlisted_global \
    nltk/test/unit/test_pickle_allowlist_security.py::test_transitionparser_loads_legitimate_model \
    nltk/test/unit/test_pickle_allowlist_security.py::test_transitionparser_rejects_malicious_model \
    nltk/test/unit/test_pickle_allowlist_security.py::test_dotted_name_attribute_traversal_blocked \
    nltk/test/unit/test_pathsec_sweep_tag.py::test_negative_control_pathsec_open_refuses_outside \
    nltk/test/unit/test_pathsec_sweep_tag.py::test_crf_set_model_file_refuses_outside_path \
    nltk/test/unit/test_pathsec_sweep_tag.py::test_crf_train_refuses_outside_path \
    nltk/test/unit/test_pathsec_sweep_tag.py::test_stanford_tag_sents_refuses_outside_model \
    nltk/test/unit/test_pathsec_sweep_tag.py::test_hunpos_init_refuses_outside_model \
    nltk/test/unit/test_pathsec_sweep_tag.py::test_validate_tool_path_rejects_option_shaped_paths \
    nltk/test/unit/test_pathsec_sweep_tag.py::test_validate_tool_path_rejects_non_regular_files \
    nltk/test/unit/test_pathsec_sweep_tag.py::test_make_staging_dir_refuses_a_path_shaped_prefix \
    nltk/test/unit/test_pathsec_sweep_tag.py::test_save_to_json_refuses_a_path_shaped_lang \
    nltk/test/unit/test_pathsec_sweep_tag.py::test_url_shaped_model_paths_are_refused

%files -f %{pyproject_files}
%doc README.md AUTHORS.md ChangeLog SECURITY.md
%license LICENSE.txt
%{_bindir}/nltk

%changelog
%autochangelog
