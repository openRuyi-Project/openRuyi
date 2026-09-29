# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nltk

Name:           python-%{srcname}
Version:        3.10.3
Release:        %autorelease
Summary:        Natural Language Toolkit
License:        Apache-2.0
URL:            https://www.nltk.org/
#!RemoteAsset:  sha256:bb9327a461c3811c2fa4900e03840401f2126adfb30c0072827c433bd2444ea4
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

%patchlist
# CVE-2026-81726 / GHSA-8mgp-746c-j5xp
# Minimal prerequisites for the upstream security commits below.
# https://github.com/nltk/nltk/commit/99ead96679eecec5a3b95fe6caaf2c1b29107b44
# https://github.com/nltk/nltk/commit/479060632c9642983eaa4a8849875967489d5ce5
# https://github.com/nltk/nltk/commit/f1b96e145ce8d525fb02cc481906147e5934cd06
# https://github.com/nltk/nltk/commit/9e6d5f05902b9aaa1221a0a565448d17a9c9b3e8
# https://github.com/nltk/nltk/commit/1504cccb117714a117730586f2dfe3b29bb150fc
# https://github.com/nltk/nltk/commit/3a8069fa00d98d467164fbec87e4c39b2f16c970
# https://github.com/nltk/nltk/commit/25b5d614c7e81254c4ad7553d9ae45a4208abd1b
1000-CVE-2026-81726-backport-security-helpers.patch
# https://github.com/nltk/nltk/pull/3759
# https://github.com/nltk/nltk/commit/2a92b71827d754ae8920261e7ed0c4bb283ab2d7
1001-CVE-2026-81726-harden-maxent-model-saves.patch
# https://github.com/nltk/nltk/pull/3757
# https://github.com/nltk/nltk/commit/a44a7af69bca87e92d9c4a701fcbbe4512e8d450
1002-CVE-2026-81726-harden-transitionparser-pickle.patch
# https://github.com/nltk/nltk/pull/3813
# https://github.com/nltk/nltk/commit/cbc98458b43de5f792f0382583c16df39e5c5117
1003-CVE-2026-81726-harden-tagger-model-paths.patch

%description
NLTK provides a broad collection of libraries and tools for natural language
processing.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -q \
    nltk/test/unit/test_maxent_ne_save_security.py \
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
