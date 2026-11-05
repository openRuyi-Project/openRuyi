# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 150a9d6ba0aa7f407aa4feeabc5f03ce9aa7e04b
%global shortcommit 150a9d6ba0aa

Name:           gn
Version:        2540
Release:        %autorelease
Summary:        Generate Ninja build files from GN descriptions
License:        BSD-3-Clause AND LicenseRef-openRuyi-Public-Domain AND Unicode-DFS-2016 AND ICU
URL:            https://gn.googlesource.com/gn/
VCS:            git:https://gn.googlesource.com/gn
#!RemoteAsset:  git+https://gn.googlesource.com/gn#%{commit}
#!CreateArchive
Source0:        %{name}-%{commit}.tar.gz

# Downstream fix for the Linux build with distribution compiler flags.
Patch2000:      2000-keep-format-checking-on-linux.patch
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-srpm-macros

%description
GN reads a project's build descriptions and emits Ninja rules for its
targets. It also lists build arguments, target relationships and files.

%prep
%autosetup -p1 -n %{name}-%{commit}
cp -p src/base/third_party/icu/LICENSE ICU-LICENSE.txt

%build
%set_build_flags
%{python3} build/gen.py --allow-warnings --no-last-commit-position --no-static-libstdc++ --no-strip
cat >out/last_commit_position.h <<'HEADER'
#define LAST_COMMIT_POSITION_NUM %{version}
#define LAST_COMMIT_POSITION "%{version} (%{shortcommit})"
HEADER
%ninja_build -C out gn gn_unittests

%install
install -Dpm 0755 out/gn %{buildroot}%{_bindir}/gn

%check
# Run the upstream command, parser and build-file generation tests.
out/gn_unittests

%files
%doc AUTHORS README.md
%license LICENSE ICU-LICENSE.txt
%{_bindir}/gn

%changelog
%autochangelog
