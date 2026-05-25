# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tools
%define go_import_path  honnef.co/go/tools

Name:           go-honnef-go-tools
Version:        0.7.0~0~dev
Release:        %autorelease
Summary:        Staticcheck tools for Go
License:        MIT
URL:            https://github.com/dominikh/go-tools
#!RemoteAsset:  sha256:0a3fa9aa78b18c225edf5984caffd782a78dc49667372c9985c21fd3901e088a
Source0:        https://github.com/dominikh/go-tools/archive/v0.7.0-0.dev.tar.gz#/%{_name}-0.7.0-0.dev.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-tools-0.7.0-0.dev

BuildRequires:  go
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/exp/typeparams)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go-golang-x-tools-go-expect
BuildRequires:  go-rpm-macros

Provides:       go(honnef.co/go/tools) = %{version}
Provides:       go(honnef.co/go/tools/analysis/callcheck) = %{version}
Provides:       go(honnef.co/go/tools/analysis/code) = %{version}
Provides:       go(honnef.co/go/tools/analysis/dfa) = %{version}
Provides:       go(honnef.co/go/tools/analysis/edit) = %{version}
Provides:       go(honnef.co/go/tools/analysis/facts/deprecated) = %{version}
Provides:       go(honnef.co/go/tools/analysis/facts/directives) = %{version}
Provides:       go(honnef.co/go/tools/analysis/facts/generated) = %{version}
Provides:       go(honnef.co/go/tools/analysis/facts/nilness) = %{version}
Provides:       go(honnef.co/go/tools/analysis/facts/purity) = %{version}
Provides:       go(honnef.co/go/tools/analysis/facts/tokenfile) = %{version}
Provides:       go(honnef.co/go/tools/analysis/facts/typedness) = %{version}
Provides:       go(honnef.co/go/tools/analysis/lint) = %{version}
Provides:       go(honnef.co/go/tools/analysis/lint/testutil) = %{version}
Provides:       go(honnef.co/go/tools/analysis/report) = %{version}
Provides:       go(honnef.co/go/tools/config) = %{version}
Provides:       go(honnef.co/go/tools/debug) = %{version}
Provides:       go(honnef.co/go/tools/go/ast/astutil) = %{version}
Provides:       go(honnef.co/go/tools/go/buildid) = %{version}
Provides:       go(honnef.co/go/tools/go/gcsizes) = %{version}
Provides:       go(honnef.co/go/tools/go/ir) = %{version}
Provides:       go(honnef.co/go/tools/go/ir/irutil) = %{version}
Provides:       go(honnef.co/go/tools/go/loader) = %{version}
Provides:       go(honnef.co/go/tools/go/types/typeutil) = %{version}
Provides:       go(honnef.co/go/tools/internal/diff/myers) = %{version}
Provides:       go(honnef.co/go/tools/internal/passes/buildir) = %{version}
Provides:       go(honnef.co/go/tools/internal/renameio) = %{version}
Provides:       go(honnef.co/go/tools/internal/robustio) = %{version}
Provides:       go(honnef.co/go/tools/internal/sharedcheck) = %{version}
Provides:       go(honnef.co/go/tools/internal/sync) = %{version}
Provides:       go(honnef.co/go/tools/internal/testenv) = %{version}
Provides:       go(honnef.co/go/tools/knowledge) = %{version}
Provides:       go(honnef.co/go/tools/lintcmd) = %{version}
Provides:       go(honnef.co/go/tools/lintcmd/cache) = %{version}
Provides:       go(honnef.co/go/tools/lintcmd/runner) = %{version}
Provides:       go(honnef.co/go/tools/lintcmd/version) = %{version}
Provides:       go(honnef.co/go/tools/pattern) = %{version}
Provides:       go(honnef.co/go/tools/printf) = %{version}
Provides:       go(honnef.co/go/tools/quickfix) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1001) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1002) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1003) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1004) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1005) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1006) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1007) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1008) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1009) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1010) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1011) = %{version}
Provides:       go(honnef.co/go/tools/quickfix/qf1012) = %{version}
Provides:       go(honnef.co/go/tools/sarif) = %{version}
Provides:       go(honnef.co/go/tools/simple) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1000) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1001) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1002) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1003) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1004) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1005) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1006) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1007) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1008) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1009) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1010) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1011) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1012) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1016) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1017) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1018) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1019) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1020) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1021) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1023) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1024) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1025) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1028) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1029) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1030) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1031) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1032) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1033) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1034) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1035) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1036) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1037) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1038) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1039) = %{version}
Provides:       go(honnef.co/go/tools/simple/s1040) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/fakejson) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/fakereflect) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/fakexml) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1000) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1001) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1002) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1003) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1004) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1005) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1006) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1007) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1008) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1010) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1011) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1012) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1013) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1014) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1015) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1016) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1017) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1018) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1019) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1020) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1021) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1023) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1024) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1025) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1026) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1027) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1028) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1029) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1030) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1031) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa1032) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa2000) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa2001) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa2002) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa2003) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa3000) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa3001) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4000) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4001) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4003) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4004) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4005) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4006) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4008) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4009) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4010) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4011) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4012) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4013) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4014) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4015) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4016) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4017) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4018) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4019) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4020) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4021) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4022) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4023) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4024) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4025) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4026) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4027) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4028) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4029) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4030) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4031) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa4032) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5000) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5001) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5002) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5003) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5004) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5005) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5007) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5008) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5009) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5010) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5011) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa5012) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa6000) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa6001) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa6002) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa6003) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa6005) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa6006) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa9001) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa9002) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa9003) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa9004) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa9005) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa9006) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa9007) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa9008) = %{version}
Provides:       go(honnef.co/go/tools/staticcheck/sa9009) = %{version}
Provides:       go(honnef.co/go/tools/structlayout) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1000) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1001) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1003) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1005) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1006) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1008) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1011) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1012) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1013) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1015) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1016) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1017) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1018) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1019) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1020) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1021) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1022) = %{version}
Provides:       go(honnef.co/go/tools/stylecheck/st1023) = %{version}
Provides:       go(honnef.co/go/tools/unused) = %{version}

Requires:       go(github.com/BurntSushi/toml)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/exp/typeparams)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/tools/go/expect)

%description
This package provides Staticcheck tools for Go.

%files
%doc README.md
%license LICENSE
%license LICENSE-THIRD-PARTY
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
