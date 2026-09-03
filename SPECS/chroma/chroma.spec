# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           chroma
%define go_import_path  github.com/alecthomas/chroma/v2

Name:           chroma
Version:        2.14.0
Release:        %autorelease
Summary:        General-purpose syntax highlighter
License:        MIT
URL:            https://github.com/alecthomas/chroma
#!RemoteAsset:  sha256:beff1d23ee8343c66f62aa30f1f18da5813018dcdff147f3ac4bdd734a908821
Source0:        https://github.com/alecthomas/chroma/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/assert/v2)
BuildRequires:  go(github.com/alecthomas/kong)
BuildRequires:  go(github.com/alecthomas/repr)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(golang.org/x/sys)

%description
Chroma is a general-purpose syntax highlighting library and command written in
pure Go and based on Pygments concepts.

%package     -n go-github-alecthomas-chroma-v2
Summary:        General-purpose syntax highlighting library for Go
BuildArch:      noarch
Provides:       go(github.com/alecthomas/chroma/v2) = %{version}
Requires:       go(github.com/alecthomas/kong)
Requires:       go(github.com/dlclark/regexp2)
Requires:       go(github.com/mattn/go-colorable)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(golang.org/x/sys)

%description -n go-github-alecthomas-chroma-v2
This package contains the reusable Chroma v2 source library, including its
lexers, formatters and styles.

# chromad is upstream's lexer-development playground and is not a released
# user-facing command. Keep the supported chroma CLI and reusable library.
%prep -a
rm -rf cmd/chromad

%build
%{go_common}
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
cd cmd/chroma
%__go build %{go_build_flags_default} -ldflags "-X main.version=%{version}" \
    -o %{_builddir}/chroma .

%install
install -D -m 0755 %{_builddir}/chroma %{buildroot}%{_bindir}/chroma
%buildsystem_golangmodules_install

%check
%{go_common}
%__go test %{shrink:%{go_test_flags_default}} ./...

%files
%doc README*
%license COPYING
%{_bindir}/chroma

%files -n go-github-alecthomas-chroma-v2
%doc README*
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
