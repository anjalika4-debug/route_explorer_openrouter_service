package core

type OpenrouteserviceError struct {
	IsOpenrouteserviceError bool
	Sdk              string
	Code             string
	Msg              string
	Ctx              *Context
	Result           any
	Spec             any
}

func NewOpenrouteserviceError(code string, msg string, ctx *Context) *OpenrouteserviceError {
	return &OpenrouteserviceError{
		IsOpenrouteserviceError: true,
		Sdk:              "Openrouteservice",
		Code:             code,
		Msg:              msg,
		Ctx:              ctx,
	}
}

func (e *OpenrouteserviceError) Error() string {
	return e.Msg
}
