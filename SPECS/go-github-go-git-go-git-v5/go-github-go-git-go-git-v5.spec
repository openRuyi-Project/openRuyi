# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-git
%define go_import_path  github.com/go-git/go-git/v5

Name:           go-github-go-git-go-git-v5
Version:        5.19.1
Release:        %autorelease
Summary:        Pure Go Git implementation
License:        Apache-2.0
URL:            https://github.com/go-git/go-git
#!RemoteAsset:  sha256:91b44587081b94cee4c379f7eaad28e660384f77c334da57cf53551e7e710596
Source0:        https://github.com/go-git/go-git/archive/refs/tags/v5.19.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The packaged go-git/gcfg is newer than upstream's pinned pseudo-version and
# accepts empty subsection names; adjust that single compatibility assertion.
Patch0:         2000-adjust-config-test-for-packaged-gcfg.patch

BuildOption(prep):  -n go-git-5.19.1
# Nested Go modules have their own module path/dependencies; skip them in %check
# so the parent package does not try to test unrelated internal tools.
# OBS workers have no outbound network and no readable host SSH known_hosts;
# these upstream transport packages exercise GitHub URLs, git daemon, host SSH
# state, or a CLI nested module build. Keep the rest of the package tests enabled.
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/cli/go-git*
    %{go_import_path}
    %{go_import_path}/plumbing/serverinfo
    %{go_import_path}/plumbing/transport/file
    %{go_import_path}/plumbing/transport/git
    %{go_import_path}/plumbing/transport/http
    %{go_import_path}/plumbing/transport/http/internal/test
    %{go_import_path}/plumbing/transport/ssh
    %{go_import_path}/plumbing/transport/ssh/internal/test
}

BuildRequires:  go
BuildRequires:  git
BuildRequires:  gnupg
BuildRequires:  go-rpm-macros
BuildRequires:  go(dario.cat/mergo)
BuildRequires:  go(github.com/ProtonMail/go-crypto)
BuildRequires:  go(github.com/ProtonMail/go-crypto/openpgp)
BuildRequires:  go(github.com/ProtonMail/go-crypto/openpgp/armor)
BuildRequires:  go(github.com/ProtonMail/go-crypto/openpgp/errors)
BuildRequires:  go(github.com/ProtonMail/go-crypto/openpgp/packet)
BuildRequires:  go(github.com/anmitsu/go-shlex)
BuildRequires:  go(github.com/armon/go-socks5)
BuildRequires:  go(github.com/cloudflare/circl)
BuildRequires:  go(github.com/cyphar/filepath-securejoin)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/elazarl/goproxy)
BuildRequires:  go(github.com/emirpasic/gods)
BuildRequires:  go(github.com/emirpasic/gods/trees/binaryheap)
BuildRequires:  go(github.com/gliderlabs/ssh)
BuildRequires:  go(github.com/go-git/gcfg)
BuildRequires:  go(github.com/go-git/go-billy/v5)
BuildRequires:  go(github.com/go-git/go-billy/v5/helper/chroot)
BuildRequires:  go(github.com/go-git/go-billy/v5/memfs)
BuildRequires:  go(github.com/go-git/go-billy/v5/osfs)
BuildRequires:  go(github.com/go-git/go-billy/v5/util)
BuildRequires:  go(github.com/go-git/go-git-fixtures/v4)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/groupcache/lru)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/jbenet/go-context)
BuildRequires:  go(github.com/jbenet/go-context/io)
BuildRequires:  go(github.com/kevinburke/ssh_config)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/pjbgf/sha1cd)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/sergi/go-diff)
BuildRequires:  go(github.com/sergi/go-diff/diffmatchpatch)
BuildRequires:  go(github.com/skeema/knownhosts)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(github.com/xanzy/ssh-agent)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/crypto/ssh)
BuildRequires:  go(golang.org/x/crypto/ssh/testdata)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/net/proxy)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/execabs)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/text/unicode/norm)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/warnings.v0)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/go-git/go-git/v5) = %{version}
Provides:       go(github.com/go-git/go-git/v5/config) = %{version}
Provides:       go(github.com/go-git/go-git/v5/internal/path_util) = %{version}
Provides:       go(github.com/go-git/go-git/v5/internal/pathutil) = %{version}
Provides:       go(github.com/go-git/go-git/v5/internal/reference) = %{version}
Provides:       go(github.com/go-git/go-git/v5/internal/revision) = %{version}
Provides:       go(github.com/go-git/go-git/v5/internal/test) = %{version}
Provides:       go(github.com/go-git/go-git/v5/internal/url) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/cache) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/color) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/filemode) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/format/commitgraph) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/format/commitgraph/v2) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/format/config) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/format/diff) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/format/gitattributes) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/format/gitignore) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/format/idxfile) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/format/index) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/format/objfile) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/format/packfile) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/format/pktline) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/hash) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/object) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/object/commitgraph) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/protocol/packp) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/protocol/packp/capability) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/protocol/packp/sideband) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/revlist) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/serverinfo) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/storer) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/transport) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/transport/client) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/transport/file) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/transport/git) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/transport/http) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/transport/http/internal/test) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/transport/internal/common) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/transport/server) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/transport/ssh) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/transport/ssh/internal/test) = %{version}
Provides:       go(github.com/go-git/go-git/v5/plumbing/transport/test) = %{version}
Provides:       go(github.com/go-git/go-git/v5/storage) = %{version}
Provides:       go(github.com/go-git/go-git/v5/storage/filesystem) = %{version}
Provides:       go(github.com/go-git/go-git/v5/storage/filesystem/dotgit) = %{version}
Provides:       go(github.com/go-git/go-git/v5/storage/memory) = %{version}
Provides:       go(github.com/go-git/go-git/v5/storage/test) = %{version}
Provides:       go(github.com/go-git/go-git/v5/storage/transactional) = %{version}
Provides:       go(github.com/go-git/go-git/v5/tests/objectverify) = %{version}
Provides:       go(github.com/go-git/go-git/v5/utils/binary) = %{version}
Provides:       go(github.com/go-git/go-git/v5/utils/diff) = %{version}
Provides:       go(github.com/go-git/go-git/v5/utils/ioutil) = %{version}
Provides:       go(github.com/go-git/go-git/v5/utils/merkletrie) = %{version}
Provides:       go(github.com/go-git/go-git/v5/utils/merkletrie/filesystem) = %{version}
Provides:       go(github.com/go-git/go-git/v5/utils/merkletrie/index) = %{version}
Provides:       go(github.com/go-git/go-git/v5/utils/merkletrie/internal/frame) = %{version}
Provides:       go(github.com/go-git/go-git/v5/utils/merkletrie/internal/fsnoder) = %{version}
Provides:       go(github.com/go-git/go-git/v5/utils/merkletrie/noder) = %{version}
Provides:       go(github.com/go-git/go-git/v5/utils/sync) = %{version}
Provides:       go(github.com/go-git/go-git/v5/utils/trace) = %{version}

Requires:       go(dario.cat/mergo)
Requires:       go(github.com/ProtonMail/go-crypto)
Requires:       go(github.com/ProtonMail/go-crypto/openpgp)
Requires:       go(github.com/ProtonMail/go-crypto/openpgp/packet)
Requires:       go(github.com/anmitsu/go-shlex)
Requires:       go(github.com/cloudflare/circl)
Requires:       go(github.com/cyphar/filepath-securejoin)
Requires:       go(github.com/elazarl/goproxy)
Requires:       go(github.com/emirpasic/gods)
Requires:       go(github.com/emirpasic/gods/trees/binaryheap)
Requires:       go(github.com/gliderlabs/ssh)
Requires:       go(github.com/go-git/gcfg)
Requires:       go(github.com/go-git/go-billy/v5)
Requires:       go(github.com/go-git/go-billy/v5/helper/chroot)
Requires:       go(github.com/go-git/go-billy/v5/osfs)
Requires:       go(github.com/go-git/go-billy/v5/util)
Requires:       go(github.com/go-git/go-git-fixtures/v4)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/groupcache/lru)
Requires:       go(github.com/jbenet/go-context)
Requires:       go(github.com/jbenet/go-context/io)
Requires:       go(github.com/kevinburke/ssh_config)
Requires:       go(github.com/klauspost/cpuid/v2)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/kr/text)
Requires:       go(github.com/pjbgf/sha1cd)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(github.com/sergi/go-diff)
Requires:       go(github.com/sergi/go-diff/diffmatchpatch)
Requires:       go(github.com/skeema/knownhosts)
Requires:       go(github.com/xanzy/ssh-agent)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/crypto/ssh)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/net/proxy)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/sys/execabs)
Requires:       go(golang.org/x/text)
Requires:       go(gopkg.in/check.v1)
Requires:       go(gopkg.in/warnings.v0)


%description
go-git is an extensible Git implementation written in Go. It provides low-level
plumbing and high-level porcelain APIs for manipulating Git repositories.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let this module own
# their source directories, otherwise RPM can hit file conflicts.
%exclude %{go_sys_gopath}/%{go_import_path}/cli/go-git

%changelog
%autochangelog
