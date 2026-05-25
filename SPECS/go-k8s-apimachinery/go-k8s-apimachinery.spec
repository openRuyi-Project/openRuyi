# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           apimachinery
%define go_import_path  k8s.io/apimachinery

Name:           go-k8s-apimachinery
Version:        1.36.0~alpha2
Release:        %autorelease
Summary:        Go module dependency for Prometheus
License:        Apache-2.0
URL:            https://github.com/kubernetes/apimachinery
#!RemoteAsset:  sha256:1d62ecdcdd5700f1d829938946650eb16fe79f3963ff81c880e437a399baa2a0
Source0:        https://github.com/kubernetes/apimachinery/archive/kubernetes-1.36.0-alpha.2.tar.gz#/%{_name}-kubernetes-1.36.0-alpha.2.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n apimachinery-kubernetes-1.36.0-alpha.2
# managedfields tests expect api/openapi-spec/swagger.json from the full
# kubernetes repository, but the standalone apimachinery archive lacks it.
%define go_test_exclude %{shrink:
    %{go_import_path}/pkg/util/managedfields
    %{go_import_path}/pkg/util/managedfields/internal
}

BuildRequires:  go
BuildRequires:  go(github.com/armon/go-socks5)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/moby/spdystream)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/mxk/go-flowrate)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/evanphx/json-patch.v4)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)
BuildRequires:  go-rpm-macros

Provides:       go(k8s.io/apimachinery) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/apitesting) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/apitesting/fuzzer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/apitesting/naming) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/apitesting/roundtrip) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/equality) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/errors) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/meta) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/meta/table) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/meta/testrestmapper) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/operation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/resource) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/safe) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/validate) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/validate/constraints) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/validate/content) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/validation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/api/validation/path) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/asn1) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/fuzzer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion/scheme) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/internalversion/validation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured/unstructuredscheme) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1/validation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1beta1) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/meta/v1beta1/validation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/testapigroup) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/testapigroup/fuzzer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/testapigroup/install) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/apis/testapigroup/v1) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/conversion) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/conversion/queryparams) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/fields) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/labels) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/schema) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/cbor) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/cbor/direct) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/cbor/internal/modes) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/json) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/protobuf) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/recognizer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/recognizer/testing) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/streaming) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/versioning) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/serializer/yaml) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/testing) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/runtime/testing/v1) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/selection) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/test) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/types) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/cache) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/diff) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/dump) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/duration) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/errors) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/framer) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/httpstream) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/httpstream/spdy) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/httpstream/wsstream) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/intstr) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/json) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/jsonmergepatch) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/managedfields) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/managedfields/internal) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/managedfields/internal/testing) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/managedfields/managedfieldstest) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/mergepatch) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/naming) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/net) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/net/testing) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/portforward) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/proxy) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/rand) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/remotecommand) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/resourceversion) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/runtime) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/sets) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/sort) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/strategicpatch) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/strategicpatch/testing) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/uuid) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/validation) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/validation/field) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/version) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/wait) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/waitgroup) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/util/yaml) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/version) = %{version}
Provides:       go(k8s.io/apimachinery/pkg/watch) = %{version}
Provides:       go(k8s.io/apimachinery/third_party/forked/golang/json) = %{version}
Provides:       go(k8s.io/apimachinery/third_party/forked/golang/netutil) = %{version}
Provides:       go(k8s.io/apimachinery/third_party/forked/golang/reflect) = %{version}

Requires:       go(github.com/armon/go-socks5)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/fxamacker/cbor/v2)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/go-openapi/jsonreference)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/google/gnostic-models)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/josharian/intern)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/moby/spdystream)
Requires:       go(github.com/modern-go/concurrent)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(github.com/mxk/go-flowrate)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/x448/float16)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/evanphx/json-patch.v4)
Requires:       go(gopkg.in/inf.v0)
Requires:       go(gopkg.in/yaml.v3)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kube-openapi)
Requires:       go(k8s.io/utils)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)
Requires:       go(sigs.k8s.io/yaml)

%description
Go module dependency for Prometheus. Generated by go2spec.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
