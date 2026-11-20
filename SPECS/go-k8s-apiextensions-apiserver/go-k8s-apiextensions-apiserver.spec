# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           apiextensions-apiserver
%define go_import_path  k8s.io/apiextensions-apiserver

Name:           go-k8s-apiextensions-apiserver
Version:        0.36.2
Release:        %autorelease
Summary:        Kubernetes custom resource API server
License:        Apache-2.0
URL:            https://github.com/kubernetes/apiextensions-apiserver
#!RemoteAsset:  sha256:a70670059ef2317f351b5f4d55e010af909382c5d8f7b765e935242e85ab6eb5
Source0:        https://github.com/kubernetes/apiextensions-apiserver/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/google/cel-go)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.etcd.io/etcd/client/v3)
BuildRequires:  go(go.opentelemetry.io/otel/attribute)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(gopkg.in/evanphx/json-patch.v4)
BuildRequires:  go(k8s.io/api/apidiscovery/v2)
BuildRequires:  go(k8s.io/api/autoscaling/v1)
BuildRequires:  go(k8s.io/api/core/v1)
BuildRequires:  go(k8s.io/apimachinery/pkg)
BuildRequires:  go(k8s.io/apimachinery/pkg/version)
BuildRequires:  go(k8s.io/apiserver/pkg)
BuildRequires:  go(k8s.io/client-go/applyconfigurations)
BuildRequires:  go(k8s.io/client-go/discovery)
BuildRequires:  go(k8s.io/client-go/dynamic)
BuildRequires:  go(k8s.io/client-go/gentype)
BuildRequires:  go(k8s.io/client-go/kubernetes)
BuildRequires:  go(k8s.io/client-go/listers)
BuildRequires:  go(k8s.io/client-go/openapi3)
BuildRequires:  go(k8s.io/client-go/rest)
BuildRequires:  go(k8s.io/client-go/restmapper)
BuildRequires:  go(k8s.io/client-go/scale)
BuildRequires:  go(k8s.io/client-go/testing)
BuildRequires:  go(k8s.io/client-go/tools)
BuildRequires:  go(k8s.io/client-go/util)
BuildRequires:  go(k8s.io/component-base/cli)
BuildRequires:  go(k8s.io/component-base/compatibility)
BuildRequires:  go(k8s.io/component-base/featuregate)
BuildRequires:  go(k8s.io/component-base/logs)
BuildRequires:  go(k8s.io/component-base/metrics)
BuildRequires:  go(k8s.io/component-base/tracing)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kube-openapi/pkg)
BuildRequires:  go(k8s.io/kube-openapi/pkg/validation)
BuildRequires:  go(k8s.io/utils/net)
BuildRequires:  go(k8s.io/utils/ptr)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)
BuildRequires:  go-rpm-macros

Provides:       go(k8s.io/apiextensions-apiserver) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/hack) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/apis/cr) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/apis/cr/v1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/applyconfiguration) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/applyconfiguration/cr/v1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/applyconfiguration/internal) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/clientset/versioned) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/clientset/versioned/fake) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/clientset/versioned/scheme) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/clientset/versioned/typed/cr/v1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/clientset/versioned/typed/cr/v1/fake) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/informers/externalversions) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/informers/externalversions/cr) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/informers/externalversions/cr/v1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/informers/externalversions/internalinterfaces) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/examples/client-go/pkg/client/listers/cr/v1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apihelpers) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/fuzzer) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/install) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apiserver) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apiserver/conversion) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apiserver/schema) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/model) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apiserver/schema/defaulting) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apiserver/schema/listtype) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apiserver/schema/objectmeta) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apiserver/schema/pruning) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/apiserver/validation) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/applyconfiguration) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/applyconfiguration/apiextensions/v1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/applyconfiguration/apiextensions/v1beta1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/applyconfiguration/internal) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/clientset/clientset) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/clientset/clientset/fake) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/clientset/clientset/scheme) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/clientset/clientset/typed/apiextensions/v1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/clientset/clientset/typed/apiextensions/v1/fake) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/clientset/clientset/typed/apiextensions/v1beta1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/clientset/clientset/typed/apiextensions/v1beta1/fake) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/informers/externalversions) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/informers/externalversions/apiextensions) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/informers/externalversions/apiextensions/v1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/informers/externalversions/apiextensions/v1beta1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/informers/externalversions/internalinterfaces) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/listers/apiextensions/v1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/client/listers/apiextensions/v1beta1) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/cmd/server) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/cmd/server/options) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/cmd/server/testing) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/controller/apiapproval) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/controller/establish) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/controller/finalizer) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/controller/nonstructuralschema) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/controller/openapi) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/controller/openapi/builder) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/controller/openapi/v2) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/controller/openapiv3) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/controller/status) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/crdserverscheme) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/features) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/generated/openapi) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/registry/customresource) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/registry/customresource/tableconvertor) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/registry/customresourcedefinition) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/pkg/test) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/test/integration) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/test/integration/conversion) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/test/integration/fixtures) = %{version}
Provides:       go(k8s.io/apiextensions-apiserver/test/integration/storage) = %{version}

Requires:       go(github.com/emicklei/go-restful/v3)
Requires:       go(github.com/google/cel-go)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.etcd.io/etcd/client/v3)
Requires:       go(go.opentelemetry.io/otel/attribute)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/grpc)
Requires:       go(k8s.io/api/apidiscovery/v2)
Requires:       go(k8s.io/api/autoscaling/v1)
Requires:       go(k8s.io/api/core/v1)
Requires:       go(k8s.io/apimachinery/pkg)
Requires:       go(k8s.io/apimachinery/pkg/version)
Requires:       go(k8s.io/apiserver/pkg)
Requires:       go(k8s.io/client-go/applyconfigurations)
Requires:       go(k8s.io/client-go/discovery)
Requires:       go(k8s.io/client-go/dynamic)
Requires:       go(k8s.io/client-go/gentype)
Requires:       go(k8s.io/client-go/kubernetes)
Requires:       go(k8s.io/client-go/listers)
Requires:       go(k8s.io/client-go/rest)
Requires:       go(k8s.io/client-go/restmapper)
Requires:       go(k8s.io/client-go/scale)
Requires:       go(k8s.io/client-go/testing)
Requires:       go(k8s.io/client-go/tools)
Requires:       go(k8s.io/client-go/util)
Requires:       go(k8s.io/component-base/cli)
Requires:       go(k8s.io/component-base/compatibility)
Requires:       go(k8s.io/component-base/featuregate)
Requires:       go(k8s.io/component-base/logs)
Requires:       go(k8s.io/component-base/metrics)
Requires:       go(k8s.io/component-base/tracing)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kube-openapi/pkg)
Requires:       go(k8s.io/kube-openapi/pkg/validation)
Requires:       go(k8s.io/utils/net)
Requires:       go(k8s.io/utils/ptr)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)

%description
This package provides the Kubernetes API extension server and libraries
for defining and serving custom resources.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
